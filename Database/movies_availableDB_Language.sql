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
-- Table structure for table `Language`
--

DROP TABLE IF EXISTS `Language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Language` (
  `language` varchar(20) NOT NULL,
  PRIMARY KEY (`language`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Language`
--

LOCK TABLES `Language` WRITE;
/*!40000 ALTER TABLE `Language` DISABLE KEYS */;
INSERT INTO `Language` VALUES (''),('Aboriginal'),('Acholi'),('Afrikaans'),('Akan'),('Albanian'),('Algonquin'),('American Sign Langua'),('Amharic'),('Ancient (to 1453)'),('Apache languages'),('Arabic'),('Aragonese'),('Aramaic'),('Armenian'),('Assamese'),('Assyrian Neo-Aramaic'),('Athapascan languages'),('Australian Sign Lang'),('Awadhi'),('Azerbaijani'),('Basque'),('Belarusian'),('Bemba'),('Bengali'),('Berber languages'),('Bhojpuri'),('Bosnian'),('Brazilian Sign Langu'),('British Sign Languag'),('Bulgarian'),('Cantonese'),('Catalan'),('Chechen'),('Cheyenne'),('Chinese'),('Cornish'),('Creek'),('Croatian'),('Czech'),('Danish'),('Dari'),('Dutch'),('Dyula'),('East-Greenlandic'),('English'),('Esperanto'),('Estonian'),('Ewe'),('Filipino'),('Finnish'),('Flemish'),('French'),('French Sign Language'),('Fulah'),('Gallegan'),('Georgian'),('German'),('Greek'),('Greenlandic'),('Guarani'),('Gujarati'),('Haitian'),('Hakka'),('Haryanvi'),('Hausa'),('Hawaiian'),('Hebrew'),('Hindi'),('Hokkien'),('Hungarian'),('Ibo'),('Icelandic'),('Indonesian'),('Inuktitut'),('Irish'),('Italian'),('Japanese'),('Japanese Sign Langua'),('Kabyle'),('Kannada'),('Kazakh'),('Khmer'),('Kinyarwanda'),('Kirghiz'),('Klingon'),('Korean'),('Kriolu'),('Kudmali'),('Kurdish'),('Lao'),('Latin'),('Latvian'),('Lingala'),('Lithuanian'),('Low German'),('Luxembourgish'),('Macedonian'),('Malay'),('Malayalam'),('Maltese'),('Mandarin'),('Manipuri'),('Maori'),('Mapudungun'),('Marathi'),('Masai'),('Maya'),('Micmac'),('Middle English'),('Min Nan'),('Minangkabau'),('Mixtec'),('Mohawk'),('Mongolian'),('More'),('Nama'),('Navajo'),('Nepali'),('None'),('North American India'),('Norwegian'),('Nushi'),('Nyanja'),('Occitan'),('Papiamento'),('Persian'),('Polish'),('Polynesian'),('Portuguese'),('Punjabi'),('Pushto'),('Quechua'),('Rajasthani'),('Romanian'),('Romany'),('Russian'),('Saami'),('Sanskrit'),('Scots'),('Scottish Gaelic'),('Serbian'),('Serbo-Croatian'),('Shanghainese'),('Sicilian'),('Sign Languages'),('Sinhalese'),('Sioux'),('Slovak'),('Slovenian'),('Somali'),('Southern Sotho'),('Spanish'),('Spanish Sign Languag'),('Swahili'),('Swedish'),('Swiss German'),('Tagalog'),('Tajik'),('Tamil'),('Tarahumara'),('Tatar'),('Telugu'),('Teochew'),('Thai'),('Tibetan'),('Tupi'),('Turkish'),('Turkmen'),('Uighur'),('Ukrainian'),('Urdu'),('Vietnamese'),('Welsh'),('Wolof'),('Xhosa'),('Yiddish'),('Yoruba'),('Zulu');
/*!40000 ALTER TABLE `Language` ENABLE KEYS */;
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

-- Dump completed on 2020-11-04 18:39:09
