CREATE DATABASE  IF NOT EXISTS `sgti`;
USE `sgti`;

DROP TABLE IF EXISTS `equipments`;

CREATE TABLE `equipments` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `place` varchar(30) NOT NULL,
  `department` varchar(30) DEFAULT NULL,
  `user` varchar(30) DEFAULT NULL,
  `office_license` varchar(45) DEFAULT NULL,
  `office_type` varchar(6) DEFAULT NULL,
  `office_key` varchar(35) DEFAULT NULL,
  `windows_license` varchar(45) DEFAULT NULL,
  `windows_type` varchar(6) DEFAULT NULL,
  `windows_key` varchar(35) DEFAULT NULL,
  `equipment` varchar(10) NOT NULL,
  `manufacturer` varchar(15) NOT NULL,
  `id_equipment` varchar(10) NOT NULL,
  `invoice` int DEFAULT NULL,
  `access_key` varchar(55) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_equipment` (`id_equipment`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

LOCK TABLES `equipments` WRITE;

INSERT INTO `equipments` VALUES (1,'Empresa 1','T.I.','Yuri Prawucki','Office 2016 Home & Business','FPP','XXXXX-XXXXX-XXXXX-XXXXX-XXXXX','Windows 10 PRO','OEM','XXXXX-XXXXX-XXXXX-XXXXX-XXXXX','Notebook','Lenovo','NTB01',6859,'41201116794775000116550010000068591000164407','Vendas Informática','2021-01-04 17:43:56');

UNLOCK TABLES;

DROP TABLE IF EXISTS `logins`;

CREATE TABLE `logins` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `username` varchar(60) NOT NULL,
  `password` varchar(20) NOT NULL,
  `reg_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

LOCK TABLES `logins` WRITE;

INSERT INTO `logins` VALUES (1,'Yuri','Prawucki','yuri.prawucki','123456','2020-12-26 21:11:54');

UNLOCK TABLES;

DROP TABLE IF EXISTS `places`;

CREATE TABLE `places` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `place` varchar(30) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `place` (`place`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

LOCK TABLES `places` WRITE;

INSERT INTO `places` VALUES (1,'Empresa 1','2021-01-04 20:43:56'),(2,'Empresa 2','2021-07-01 01:51:43');

UNLOCK TABLES;

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `full_name` varchar(60) NOT NULL,
  `occupation` varchar(60) NOT NULL,
  `place` varchar(30) NOT NULL,
  `email` varchar(60) DEFAULT NULL,
  `pass_email` varchar(60) DEFAULT NULL,
  `skype` varchar(60) DEFAULT NULL,
  `pass_skype` varchar(60) DEFAULT NULL,
  `google_account` varchar(6) DEFAULT NULL,
  `sistema_autcom` varchar(6) DEFAULT NULL,
  `sistema_sgr` varchar(6) DEFAULT NULL,
  `sistema_express` varchar(6) DEFAULT NULL,
  `login_systems` varchar(6) DEFAULT NULL,
  `pass_systems` varchar(10) DEFAULT NULL,
  `inactive` varchar(6) DEFAULT NULL,
  `reg_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `full_name` (`full_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

LOCK TABLES `users` WRITE;

INSERT INTO `users` VALUES (1,'Yuri Prawucki','Tecnologia','Empresa 1','yuri@tecnologia.com.br','123mudar','yuri@tecnologia.com.br','123mudar','Sim','1','1','1','456','98765','Não','2021-06-30 02:21:02');

UNLOCK TABLES;

CREATE USER IF NOT EXISTS 'sgtiuser'@'localhost' IDENTIFIED BY 'sgtipass';
GRANT ALL PRIVILEGES ON sgti.* TO 'sgtiuser'@'localhost';
FLUSH PRIVILEGES;