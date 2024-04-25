from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import pymysql.cursors
import uuid
import jwt
import secrets

token_data = {}

app = FastAPI()
# Database connection settings
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='#Nawu#*13',
                             database='api',
                             cursorclass=pymysql.cursors.DictCursor)

# Security settings
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str = None

class Job(BaseModel):
    job_id: str
    user_id: str
    status: str

# Database operations
def get_user(email: str):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users WHERE email = %s"
        cursor.execute(sql, (email,))
        return cursor.fetchone()

def create_job(job: Job):
    with connection.cursor() as cursor:
        sql = "INSERT INTO jobs (job_id, user_id, status) VALUES (%s, %s, %s)"
        cursor.execute(sql, (job.job_id, job.user_id, job.status))
        connection.commit()

def get_user_credits(user_id: str):
    with connection.cursor() as cursor:
        sql = "SELECT credits FROM user_credits WHERE user_id = %s"
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()
        if result:
            return result['credits']
        else:
            return 0

def deduct_credits(user_id: str, amount: int):
    with connection.cursor() as cursor:
        sql = "UPDATE user_credits SET credits = credits - %s WHERE user_id = %s"
        cursor.execute(sql, (amount, user_id))
        connection.commit()

# Authentication
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(email: str):
    user = get_user(email)
    if user:
        return User(**user)

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# API endpoints
@app.post("/submit_job")
async def submit_job(job: Job, token: str = Depends(oauth2_scheme)):
    # Authenticate user based on token
    user = get_user_by_email(token_data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Check user credits and queue job if enough credits available
    credits_needed = 10  # Example: 10 credits needed for a job
    user_credits = get_user_credits(user.user_id)
    if user_credits < credits_needed:
        raise HTTPException(status_code=403, detail="Insufficient credits")
    
    
    # Deduct credits from user account
    deduct_credits(user.user_id, credits_needed)
    
    # Save job to database
    job.job_id = str(uuid.uuid4())
    job.user_id = user.user_id
    job.status = "queued"
    create_job(job)
    
    return {"message": "Job submitted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
