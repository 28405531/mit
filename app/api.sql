-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 26, 2024 at 08:00 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `api`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `email`, `password`, `timestamp`) VALUES
(1, '[admin@gmail.com]', '[123]', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `job_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`) VALUES
(1, 'a@gmail.com', 'pbkdf2:sha256:600000$vmxzTxUR7Wg1f3y6$92771cf6065d8cf669b991a4a5f09d037a31ca425b599bfd54c3f700880396'),
(2, 'k@gmail.com', 'pbkdf2:sha256:600000$VS9167zMpqS2tceL$2b55d899d5c6fac23fbb5c60a302ebb27236e3af486cd90fb279b36983499c'),
(3, 'arain@gmail.com', 'pbkdf2:sha256:600000$Cvr81qq6BkipS1O1$6170f62520ab0d448ad5cccf38cf5b790d4ca0b2f69f2df131340bb1de6222'),
(4, 'b@gmail.com', 'pbkdf2:sha256:600000$FiMjOVIda9bWNHEX$da2695dc955508018de84e185f296f20ce0d08d77e53898d83d4547b2363f4'),
(5, 'm@gmail.com', 'pbkdf2:sha256:600000$UHXJ56PrwDS4GxM4$0261baa4c697a3bf2f61ddbe7f6540ea8ce732c7f791e111763c8b2bb00177'),
(6, 'ali@gmail.com', 'scrypt:32768:8:1$Ijsu69ZiiSd3R5gJ$1edfed431cde577b33cad422076139242eb766c9cd1e5cedc5642ff50990bc23147bc0c41b01f75adddc303bbb8c81a043fd7d02eb3f0f876eb082480ad34b55'),
(7, 'kamran@gmail.com', 'pbkdf2:sha256:260000$CsvIOlb1xQ7do9F9$1cf0d5f61bb62c74395fb654c272313b072954f88005e06f3045deecd4b751dc'),
(8, 'rizwan@gmail.com', 'pbkdf2:sha256:260000$uMACDlVUjFNcZ5xN$f7230a7d87650afc0f5d30a6f97dfd02a752e92ddfbbd98a10731ac913e5054c'),
(9, 'rizu@gmail.com', 'pbkdf2:sha256:260000$idChGEhRRFdVxOGS$25962f0cf15be0848420cb78f742af66e1cd9e450d946da503e6bffbc86da27e');

-- --------------------------------------------------------

--
-- Table structure for table `user_credits`
--

CREATE TABLE `user_credits` (
  `user_id` int(11) NOT NULL,
  `credits` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`job_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`email`);

--
-- Indexes for table `user_credits`
--
ALTER TABLE `user_credits`
  ADD KEY `id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `jobs`
--
ALTER TABLE `jobs`
  ADD CONSTRAINT `jobs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `user_credits`
--
ALTER TABLE `user_credits`
  ADD CONSTRAINT `user_credits_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
