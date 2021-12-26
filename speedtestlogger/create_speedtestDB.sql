CREATE DATABASE IF NOT EXISTS speedtestDB;
USE speedtestDB;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE IF NOT EXISTS test_result(
    
    testTimestamp datetime not null,
    downloadSpeed double not null,
    uploadSpeed double not null,
    
    constraint primary key(testTimestamp)
    
) engine=innodb;