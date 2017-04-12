tee /tmp/temp.log
drop database if exists lu;
create database lu;
use lu;
/*drop TABLE if exists hostname;*/
CREATE TABLE if not EXISTS userinfo `hostname` (
  `H_id` tinyint(4) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(20) NOT NULL,
  `ip` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `system` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY(H_id,hostname)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*drop table if EXISTS userinfo;*/
CREATE TABLE if not EXISTS `userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Iphone` varchar(12) NOT NULL,
  `Addr` longtext NOT NULL,
  `Admin` int(11) NOT NULL,
  `Register` date NOT NULL,
  PRIMARY KEY(id,Username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*drop table if EXISTS container;*/
create table if not EXISTS `container` (
  `C_id` tinyint(4) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `ip` varchar(15) NOT NULL,
  `createTime` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `limit` tinyint(3),
  `U_id` int(11) not null,
  `H_id` tinyint(4) not null,
  PRIMARY KEY(C_id,Name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*alter table container drop CONSTRAINT container_username;*/
alter table container add CONSTRAINT container_username foreign key (U_id) references userinfo(id);
/*alter table container drop CONSTRAINT container_hostname;*/
alter table container add CONSTRAINT container_hostname foreign key (H_id) references hostname(H_id);
