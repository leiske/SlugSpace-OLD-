# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.7.21)
# Database: slugspace
# Generation Time: 2018-01-21 00:39:19 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table parking_events
# ------------------------------------------------------------

DROP TABLE IF EXISTS `parking_events`;

CREATE TABLE `parking_events` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `lot_id` int(11) NOT NULL,
  `entered` tinyint(1) NOT NULL,
  `capacity` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `parking_events` WRITE;
/*!40000 ALTER TABLE `parking_events` DISABLE KEYS */;

INSERT INTO `parking_events` (`id`, `lot_id`, `entered`, `capacity`, `created_at`)
VALUES
	(1,1,1,17,'2018-01-20 13:55:27'),
	(2,2,1,14,'2018-01-20 13:55:27'),
	(3,2,0,15,'2018-01-20 13:55:27'),
	(4,1,0,18,'2018-01-20 14:35:00');

/*!40000 ALTER TABLE `parking_events` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table parking_lots
# ------------------------------------------------------------

DROP TABLE IF EXISTS `parking_lots`;

CREATE TABLE `parking_lots` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  `image_url` varchar(255) NOT NULL DEFAULT '',
  `filled` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `parking_lots` WRITE;
/*!40000 ALTER TABLE `parking_lots` DISABLE KEYS */;

INSERT INTO `parking_lots` (`id`, `name`, `image_url`, `filled`, `capacity`, `created_at`, `updated_at`)
VALUES
	(1,'West','image_url',2,100,'2018-01-20 13:55:27','2018-01-20 13:55:27'),
	(2,'East','image_url',5,200,'2018-01-20 13:55:27','2018-01-20 13:55:27'),
	(3,'North','image_url',10,50,'2018-01-20 13:55:27','2018-01-20 13:55:27');

/*!40000 ALTER TABLE `parking_lots` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
