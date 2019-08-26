DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `team_user_id_fk` (`user_id`),
  CONSTRAINT `team_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL DEFAULT '',
  `email` varchar(45) NOT NULL DEFAULT '',
  `type` enum('MANAGER','CUSTOMER') DEFAULT NULL,
  `encrypted_password` varchar(45) NOT NULL DEFAULT '',
  `user_salt` varchar(45) NOT NULL DEFAULT '',
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (15,'Ameen','ameen123@ddaf.com','MANAGER','ass','ass','2019-08-12 15:39:05','2019-08-12 15:39:05'),(17,'Ameen','ameen@post_test1.com','CUSTOMER','0daf1a73c90454d6240843902e7bcb37','TOoFPCRZoFQqTJ6d1MYY35s5eHZKHNcJtQPY5o0qQgUFy','2019-08-16 21:39:47','2019-08-16 21:39:47'),(27,'Ameen','ameen@post_tes22t.com','CUSTOMER','6ee38ba5bfd7485e1e18cb2f688a7159','EhI2LDPsV7ZGlWlRnrhpFV0Zalkupb8AhoekoT4ZcNVkF','2019-08-21 19:06:06','2019-08-21 19:06:06'),(28,'Ameen','ameen@post_tes23t.com','CUSTOMER','80ef16be7a0ddbea410691f57f96187e','SnzLKHpqjN4R342TzVkzX8L9Pds9Xi2Gq1HPa5U0ydwlB','2019-08-21 19:26:28','2019-08-21 19:26:28'),(29,'Ameen','ameen@post_tes24t.com','CUSTOMER','fb179fef08a008d445262bd7da073056','ENnf2Mh5AAo4HmbUYg23Pxlm74KNsXs9AcdrHp1MSdIqJ','2019-08-21 19:35:52','2019-08-21 19:35:52'),(30,'Ameen','ameen@post_tes25t.com','CUSTOMER','5e61c85b9b8cb47281d825abe8ea49e8','jVovq8uIiE4c0Q8Ky0p23sHJNMqgyczTjS4qfdSMyF80e','2019-08-21 19:36:34','2019-08-21 19:36:34'),(31,'Ameen','ameen@post_tes26t.com','CUSTOMER','491ed21fc1afa46f146d66e6525ad5c2','LPghMpINnQ2sj0VQcEAlwoThdtz6Eso2MbMXgOpAfp0BE','2019-08-21 19:37:55','2019-08-21 19:37:55'),(32,'Ameen','ameen@post_tes33t.com','CUSTOMER','5ff2636d3c491b979d21271546841dd4','nu5e1ApnDs9qwOngZCYzIOTTNb2ym22Pfqm3Dsd25z2z7','2019-08-21 21:33:30','2019-08-21 21:33:30');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tittle` varchar(45) NOT NULL DEFAULT '',
  `status` enum('ONPROGRESS','COMPLITED') DEFAULT NULL,
  `target` enum('USER','TEAM') DEFAULT NULL,
  `from_date` datetime DEFAULT NULL,
  `to_date` datetime DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `task_team_id_fk` (`team_id`),
  KEY `task_user_id_fk` (`user_id`),
  CONSTRAINT `task_team_id_fk` FOREIGN KEY (`team_id`) REFERENCES `team` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `task_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,'first task',NULL,NULL,NULL,NULL,NULL,31,NULL,NULL);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;

UNLOCK TABLES;
--
-- Table structure for table `user_address`
--

DROP TABLE IF EXISTS `user_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_address_user_id_fk` (`user_id`),
  CONSTRAINT `user_address_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_address`
--

LOCK TABLES `user_address` WRITE;
/*!40000 ALTER TABLE `user_address` DISABLE KEYS */;
INSERT INTO `user_address` VALUES (1,31,'aa',33,22,'2019-08-21 21:33:30','2019-08-21 21:33:30');
/*!40000 ALTER TABLE `user_address` ENABLE KEYS */;
UNLOCK TABLES;