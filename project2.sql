CREATE DATABASE  IF NOT EXISTS `project2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project2`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: project2
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `username` varchar(10) DEFAULT NULL,
  `pwd` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `booking_seats`
--

DROP TABLE IF EXISTS `booking_seats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking_seats` (
  `bs_id` int NOT NULL AUTO_INCREMENT,
  `b_id` int DEFAULT NULL,
  `s_id` int DEFAULT NULL,
  `se_id` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  `bs_status` varchar(10) DEFAULT '1',
  PRIMARY KEY (`bs_id`),
  KEY `b_id` (`b_id`),
  CONSTRAINT `booking_seats_ibfk_1` FOREIGN KEY (`b_id`) REFERENCES `bookings` (`b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `b_id` int NOT NULL AUTO_INCREMENT,
  `c_id` int DEFAULT NULL,
  `s_id` int DEFAULT NULL,
  PRIMARY KEY (`b_id`),
  KEY `s_id` (`s_id`),
  KEY `c_id` (`c_id`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`s_id`) REFERENCES `shows` (`s_id`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `customers` (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `city_id` int NOT NULL AUTO_INCREMENT,
  `pincode` decimal(10,0) DEFAULT NULL,
  `c_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`city_id`),
  UNIQUE KEY `pincode` (`pincode`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `c_id` int NOT NULL AUTO_INCREMENT,
  `c_name` varchar(20) DEFAULT NULL,
  `c_email` varchar(100) DEFAULT NULL,
  `c_mobile` varchar(10) DEFAULT NULL,
  `c_password` varchar(20) DEFAULT NULL,
  `c_gender` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`c_id`),
  UNIQUE KEY `c_name` (`c_name`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `m_id` int NOT NULL AUTO_INCREMENT,
  `m_name` varchar(100) DEFAULT NULL,
  `m_desc` varchar(300) DEFAULT NULL,
  `m_genre` varchar(100) DEFAULT NULL,
  `m_year` year DEFAULT NULL,
  `m_length` varchar(20) DEFAULT NULL,
  `m_rating` decimal(3,1) DEFAULT '10.0',
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `seats`
--

DROP TABLE IF EXISTS `seats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seats` (
  `se_id` int NOT NULL,
  `t_id` int NOT NULL,
  `se_type` varchar(20) DEFAULT 'f',
  `se_price` float DEFAULT '100',
  PRIMARY KEY (`se_id`,`t_id`),
  KEY `t_id` (`t_id`),
  CONSTRAINT `seats_ibfk_1` FOREIGN KEY (`t_id`) REFERENCES `theater` (`t_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shows` (
  `s_id` int NOT NULL AUTO_INCREMENT,
  `t_id` int DEFAULT NULL,
  `m_id` int DEFAULT NULL,
  `s_date` date DEFAULT NULL,
  `s_start` time DEFAULT NULL,
  `s_end` time DEFAULT NULL,
  `s_status` varchar(10) DEFAULT '1',
  PRIMARY KEY (`s_id`),
  KEY `t_id` (`t_id`),
  KEY `m_id` (`m_id`),
  CONSTRAINT `shows_ibfk_1` FOREIGN KEY (`t_id`) REFERENCES `theater` (`t_id`),
  CONSTRAINT `shows_ibfk_2` FOREIGN KEY (`m_id`) REFERENCES `movies` (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_owner`
--

DROP TABLE IF EXISTS `t_owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_owner` (
  `o_id` int NOT NULL AUTO_INCREMENT,
  `o_name` varchar(100) DEFAULT NULL,
  `o_dob` date DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `id_type` varchar(100) DEFAULT NULL,
  `id_num` varchar(100) DEFAULT NULL,
  `o_mobile` varchar(10) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `o_pass` varchar(10) NOT NULL,
  `o_status` varchar(10) DEFAULT '1',
  PRIMARY KEY (`o_id`),
  UNIQUE KEY `o_name` (`o_name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `theater`
--

DROP TABLE IF EXISTS `theater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `theater` (
  `t_id` int NOT NULL AUTO_INCREMENT,
  `t_name` varchar(100) DEFAULT NULL,
  `t_rating` decimal(3,1) DEFAULT '10.0',
  `t_status` varchar(10) DEFAULT '1',
  `c_id` int DEFAULT NULL,
  `o_id` int DEFAULT NULL,
  `e_year` year DEFAULT NULL,
  PRIMARY KEY (`t_id`),
  KEY `c_id` (`c_id`),
  KEY `o_id` (`o_id`),
  CONSTRAINT `theater_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `city` (`city_id`),
  CONSTRAINT `theater_ibfk_2` FOREIGN KEY (`o_id`) REFERENCES `t_owner` (`o_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-18 13:06:35
