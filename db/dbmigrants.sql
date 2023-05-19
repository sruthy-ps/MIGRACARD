/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 10.4.21-MariaDB : Database - dbmigrants
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dbmigrants` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `dbmigrants`;

/*Table structure for table `tblcomplaint` */

DROP TABLE IF EXISTS `tblcomplaint`;

CREATE TABLE `tblcomplaint` (
  `compId` int(11) NOT NULL AUTO_INCREMENT,
  `uEmail` varchar(50) NOT NULL,
  `pEmail` varchar(50) NOT NULL,
  `compDetails` varchar(100) NOT NULL,
  `culpritHeight` varchar(50) NOT NULL,
  `culpritWeight` varchar(50) NOT NULL,
  `compPlace` varchar(50) NOT NULL,
  `compLat` varchar(50) NOT NULL,
  `compLon` varchar(50) NOT NULL,
  `compStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`compId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Table structure for table `tblcontractor` */

DROP TABLE IF EXISTS `tblcontractor`;

CREATE TABLE `tblcontractor` (
  `conName` varchar(50) NOT NULL,
  `conAddress` varchar(50) NOT NULL,
  `conPhone` varchar(10) NOT NULL,
  `conEmail` varchar(50) NOT NULL,
  `conLicense` varchar(50) NOT NULL,
  `conCertificate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tblcriminal` */

DROP TABLE IF EXISTS `tblcriminal`;

CREATE TABLE `tblcriminal` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `station` varchar(55) DEFAULT NULL,
  `person` varchar(55) DEFAULT NULL,
  `age` varchar(55) DEFAULT NULL,
  `gender` varchar(55) DEFAULT NULL,
  `height` varchar(55) DEFAULT NULL,
  `weight` varchar(55) DEFAULT NULL,
  `complexion` varchar(55) DEFAULT NULL,
  `place` varchar(55) DEFAULT NULL,
  `imark` varchar(55) DEFAULT NULL,
  `phone` varchar(55) DEFAULT NULL,
  `uname` varchar(55) DEFAULT NULL,
  `case` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Table structure for table `tblfeedback` */

DROP TABLE IF EXISTS `tblfeedback`;

CREATE TABLE `tblfeedback` (
  `fId` int(11) NOT NULL AUTO_INCREMENT,
  `workId` int(11) NOT NULL,
  `fdate` date NOT NULL,
  `feedback` varchar(100) NOT NULL,
  PRIMARY KEY (`fId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Table structure for table `tblglobalid` */

DROP TABLE IF EXISTS `tblglobalid`;

CREATE TABLE `tblglobalid` (
  `globalId` int(11) NOT NULL AUTO_INCREMENT,
  `labId` int(11) NOT NULL,
  `dateIssue` date NOT NULL,
  `idStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`globalId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Table structure for table `tbllabour` */

DROP TABLE IF EXISTS `tbllabour`;

CREATE TABLE `tbllabour` (
  `labId` int(11) NOT NULL AUTO_INCREMENT,
  `pEmail` varchar(50) NOT NULL,
  `labName` varchar(50) NOT NULL,
  `labAddress` varchar(50) NOT NULL,
  `labPlace` varchar(50) NOT NULL,
  `labIdMark1` varchar(100) NOT NULL,
  `labIdMark2` varchar(100) NOT NULL,
  `labPhone` varchar(10) NOT NULL,
  `labAadhar` varchar(12) NOT NULL,
  `labPhoto` varchar(100) NOT NULL,
  `labHeight` varchar(10) NOT NULL,
  `labWeight` varchar(10) NOT NULL,
  `labColor` varchar(50) NOT NULL,
  `labDisease` varchar(100) NOT NULL,
  `conEmail` varchar(50) DEFAULT NULL,
  `signature` varchar(100) NOT NULL,
  `aadharfile` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `work` varchar(50) NOT NULL,
  PRIMARY KEY (`labId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Table structure for table `tbllogin` */

DROP TABLE IF EXISTS `tbllogin`;

CREATE TABLE `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tblpolicestation` */

DROP TABLE IF EXISTS `tblpolicestation`;

CREATE TABLE `tblpolicestation` (
  `pName` varchar(50) NOT NULL,
  `pStationCode` varchar(50) NOT NULL,
  `pAddress` varchar(50) NOT NULL,
  `pCircle` varchar(50) NOT NULL,
  `pContact` varchar(10) NOT NULL,
  `pEmail` varchar(50) NOT NULL,
  PRIMARY KEY (`pEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tbltender` */

DROP TABLE IF EXISTS `tbltender`;

CREATE TABLE `tbltender` (
  `reqId` int(11) NOT NULL AUTO_INCREMENT,
  `uEmail` varchar(50) NOT NULL,
  `reqDescription` varchar(100) NOT NULL,
  `reqDate` datetime NOT NULL,
  `reqPlace` varchar(50) NOT NULL,
  `reqLat` varchar(10) NOT NULL,
  `reqLon` varchar(10) NOT NULL,
  `reqStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`reqId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Table structure for table `tbltendercall` */

DROP TABLE IF EXISTS `tbltendercall`;

CREATE TABLE `tbltendercall` (
  `tcId` int(11) NOT NULL AUTO_INCREMENT,
  `reqId` int(11) NOT NULL,
  `conEmail` varchar(50) NOT NULL,
  `tenAmt` bigint(20) NOT NULL,
  `tenSdate` varchar(50) NOT NULL,
  `tenEdate` varchar(50) NOT NULL,
  `tenDescription` varchar(100) NOT NULL,
  `tenStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`tcId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Table structure for table `tbluser` */

DROP TABLE IF EXISTS `tbluser`;

CREATE TABLE `tbluser` (
  `uName` varchar(50) NOT NULL,
  `uEmail` varchar(50) NOT NULL,
  `uContact` varchar(50) NOT NULL,
  `uAadhar` varchar(50) NOT NULL,
  PRIMARY KEY (`uEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `tblworkdetails` */

DROP TABLE IF EXISTS `tblworkdetails`;

CREATE TABLE `tblworkdetails` (
  `workId` int(11) NOT NULL AUTO_INCREMENT,
  `tcId` int(11) NOT NULL,
  `workAmt` bigint(20) NOT NULL,
  `wSdate` date NOT NULL,
  `wEdate` date DEFAULT NULL,
  `wStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`workId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Table structure for table `tblworklabors` */

DROP TABLE IF EXISTS `tblworklabors`;

CREATE TABLE `tblworklabors` (
  `wlId` int(11) NOT NULL AUTO_INCREMENT,
  `workId` int(11) NOT NULL,
  `globalId` bigint(20) NOT NULL,
  PRIMARY KEY (`wlId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
