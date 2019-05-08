-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 08, 2019 at 03:23 PM
-- Server version: 10.1.23-MariaDB-9+deb9u1
-- PHP Version: 7.0.33-0+deb9u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `BeerDB`
--
CREATE DATABASE IF NOT EXISTS `BeerDB` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `BeerDB`;

-- --------------------------------------------------------

--
-- Table structure for table `BREW_INFO`
--

CREATE TABLE `BREW_INFO` (
  `BrewID` int(11) NOT NULL,
  `BrewName` text NOT NULL,
  `Brewer` text NOT NULL,
  `OG` float NOT NULL,
  `TargetFG` float NOT NULL,
  `TargetTemp` int(11) NOT NULL,
  `IsActive` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BREW_INFO`
--

INSERT INTO `BREW_INFO` (`BrewID`, `BrewName`, `Brewer`, `OG`, `TargetFG`, `TargetTemp`, `IsActive`) VALUES
(5, 'IPA', 'nogu', 1.059, 1.009, 25, 0);

-- --------------------------------------------------------

--
-- Table structure for table `MEASUREMENTS`
--

CREATE TABLE `MEASUREMENTS` (
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `BrewID` int(11) NOT NULL,
  `SG` float NOT NULL,
  `Temperature` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `BREW_INFO`
--
ALTER TABLE `BREW_INFO`
  ADD PRIMARY KEY (`BrewID`);

--
-- Indexes for table `MEASUREMENTS`
--
ALTER TABLE `MEASUREMENTS`
  ADD KEY `BrewID` (`BrewID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `BREW_INFO`
--
ALTER TABLE `BREW_INFO`
  MODIFY `BrewID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `MEASUREMENTS`
--
ALTER TABLE `MEASUREMENTS`
  ADD CONSTRAINT `BrewID` FOREIGN KEY (`BrewID`) REFERENCES `BREW_INFO` (`BrewId`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
