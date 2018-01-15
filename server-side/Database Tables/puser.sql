-- phpMyAdmin SQL Dump
-- version 4.1.14.8
-- http://www.phpmyadmin.net
--

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


-- --------------------------------------------------------

--
-- Table structure for table `puser`
--

CREATE TABLE IF NOT EXISTS `puser` (
  `puserid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(255) COLLATE latin1_general_ci NOT NULL,
  `identity` varchar(255) COLLATE latin1_general_ci NOT NULL,
  `comp` varchar(255) COLLATE latin1_general_ci NOT NULL,
  `online` enum('0','1') COLLATE latin1_general_ci NOT NULL DEFAULT '0',
  `onlinechat` enum('0','1') COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`puserid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=12 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
