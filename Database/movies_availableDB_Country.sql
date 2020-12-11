-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: movies-on-streaming-platforms.ciwwpovuascr.us-east-1.rds.amazonaws.com    Database: movies_availableDB
-- ------------------------------------------------------
-- Server version	8.0.20

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `Country`
--

DROP TABLE IF EXISTS `Country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Country` (
  `country` varchar(20) NOT NULL,
  PRIMARY KEY (`country`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Country`
--

LOCK TABLES `Country` WRITE;
/*!40000 ALTER TABLE `Country` DISABLE KEYS */;
INSERT INTO `Country` VALUES (''),('Afghanistan'),('Albania'),('Algeria'),('Angola'),('Argentina'),('Armenia'),('Aruba'),('Australia'),('Austria'),('Azerbaijan'),('Bahamas'),('Bahrain'),('Bangladesh'),('Belarus'),('Belgium'),('Bermuda'),('Bolivia'),('Bosnia and Herzegovi'),('Botswana'),('Brazil'),('Bulgaria'),('Burkina Faso'),('Burundi'),('C?¥te d\'Ivoire'),('Cambodia'),('Cameroon'),('Canada'),('Cayman Islands'),('Chad'),('Chile'),('China'),('Colombia'),('Congo'),('Costa Rica'),('Croatia'),('Cuba'),('Cyprus'),('Czech Republic'),('Czechoslovakia'),('Denmark'),('Djibouti'),('Dominican Republic'),('East Germany'),('Ecuador'),('Egypt'),('El Salvador'),('Equatorial Guinea'),('Estonia'),('Ethiopia'),('Federal Republic of '),('Finland'),('France'),('Georgia'),('Germany'),('Ghana'),('Greece'),('Guam'),('Guatemala'),('Haiti'),('Holy See (Vatican Ci'),('Honduras'),('Hong Kong'),('Hungary'),('Iceland'),('India'),('Indonesia'),('Iran'),('Iraq'),('Ireland'),('Isle Of Man'),('Israel'),('Italy'),('Jamaica'),('Japan'),('Jordan'),('Kazakhstan'),('Kenya'),('Korea'),('Kosovo'),('Kuwait'),('Kyrgyzstan'),('Laos'),('Latvia'),('Lebanon'),('Liberia'),('Libya'),('Liechtenstein'),('Lithuania'),('Luxembourg'),('Macao'),('Malawi'),('Malaysia'),('Mali'),('Malta'),('Mexico'),('Moldova'),('Monaco'),('Mongolia'),('Montenegro'),('Morocco'),('Mozambique'),('Namibia'),('Nepal'),('Netherlands'),('New Zealand'),('Nicaragua'),('Nigeria'),('Norway'),('Oman'),('Pakistan'),('Palestine'),('Panama'),('Papua New Guinea'),('Paraguay'),('Peru'),('Philippines'),('Poland'),('Portugal'),('Puerto Rico'),('Qatar'),('Republic of North Ma'),('Reunion'),('Romania'),('Russia'),('Rwanda'),('Saudi Arabia'),('Senegal'),('Serbia'),('Serbia and Montenegr'),('Sierra Leone'),('Singapore'),('Slovakia'),('Slovenia'),('Somalia'),('South Africa'),('South Korea'),('Soviet Union'),('Spain'),('Sri Lanka'),('Sudan'),('Swaziland'),('Sweden'),('Switzerland'),('Syria'),('Taiwan'),('Tajikistan'),('Tanzania'),('Thailand'),('The Democratic Repub'),('Tonga'),('Trinidad and Tobago'),('Tunisia'),('Turkey'),('U.S. Virgin Islands'),('Uganda'),('Ukraine'),('United Arab Emirates'),('United Kingdom'),('United States'),('Uruguay'),('Vanuatu'),('Venezuela'),('Vietnam'),('West Germany'),('Yemen'),('Yugoslavia'),('Zambia'),('Zimbabwe');
/*!40000 ALTER TABLE `Country` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-04 18:39:12
