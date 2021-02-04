/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 80023
Source Host           : localhost:3306
Source Database       : db_student

Target Server Type    : MYSQL
Target Server Version : 80023
File Encoding         : 65001

Date: 2021-02-04 16:09:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_class
-- ----------------------------
DROP TABLE IF EXISTS `tb_class`;
CREATE TABLE `tb_class` (
  `classID` int NOT NULL,
  `gradeID` int NOT NULL,
  `className` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_class
-- ----------------------------
INSERT INTO `tb_class` VALUES ('1', '1', '一班');
INSERT INTO `tb_class` VALUES ('2', '1', '二班');
INSERT INTO `tb_class` VALUES ('3', '1', '三班');
INSERT INTO `tb_class` VALUES ('4', '2', '一班');
INSERT INTO `tb_class` VALUES ('5', '2', '二班');

-- ----------------------------
-- Table structure for tb_examkinds
-- ----------------------------
DROP TABLE IF EXISTS `tb_examkinds`;
CREATE TABLE `tb_examkinds` (
  `kindID` int NOT NULL,
  `kindName` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`kindID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_examkinds
-- ----------------------------
INSERT INTO `tb_examkinds` VALUES ('1', '期中考试');
INSERT INTO `tb_examkinds` VALUES ('2', '期末考试');

-- ----------------------------
-- Table structure for tb_grade
-- ----------------------------
DROP TABLE IF EXISTS `tb_grade`;
CREATE TABLE `tb_grade` (
  `gradeID` int NOT NULL DEFAULT '1',
  `gradeName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`gradeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_grade
-- ----------------------------
INSERT INTO `tb_grade` VALUES ('1', '初一');
INSERT INTO `tb_grade` VALUES ('2', '初二');
INSERT INTO `tb_grade` VALUES ('3', '初三');

-- ----------------------------
-- Table structure for tb_result
-- ----------------------------
DROP TABLE IF EXISTS `tb_result`;
CREATE TABLE `tb_result` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `stuID` varchar(20) DEFAULT NULL,
  `kindID` int DEFAULT NULL,
  `subID` int DEFAULT NULL,
  `result` double DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_result
-- ----------------------------
INSERT INTO `tb_result` VALUES ('1', 'BS0101001', '1', '1', '80');
INSERT INTO `tb_result` VALUES ('2', 'BS0101001', '1', '2', '85');
INSERT INTO `tb_result` VALUES ('3', 'BS0101001', '1', '3', '100');
INSERT INTO `tb_result` VALUES ('4', 'BS0101002', '1', '3', '100');
INSERT INTO `tb_result` VALUES ('5', 'BS0101002', '1', '1', '90');
INSERT INTO `tb_result` VALUES ('6', 'BS0101002', '1', '2', '98');

-- ----------------------------
-- Table structure for tb_student
-- ----------------------------
DROP TABLE IF EXISTS `tb_student`;
CREATE TABLE `tb_student` (
  `stuID` varchar(20) NOT NULL DEFAULT 'SID00101001',
  `stuName` varchar(20) DEFAULT NULL,
  `classID` int DEFAULT NULL,
  `gradeID` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` char(4) DEFAULT NULL,
  `phone` char(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stuID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_student
-- ----------------------------
INSERT INTO `tb_student` VALUES ('BS0101001', '小王', '1', '1', '20', '男', '1200000000', '北京市朝阳区');
INSERT INTO `tb_student` VALUES ('BS0101002', '小明', '1', '1', '21', '男', '1300000000', '天津市');
INSERT INTO `tb_student` VALUES ('BS0102001', '小花', '2', '1', '21', '女', '1400000000', '山西省太原市');
INSERT INTO `tb_student` VALUES ('BS0201001', '小红', '4', '2', '19', '女', '1500000000', '河南省郑州市');

-- ----------------------------
-- Table structure for tb_subject
-- ----------------------------
DROP TABLE IF EXISTS `tb_subject`;
CREATE TABLE `tb_subject` (
  `subID` int NOT NULL,
  `subName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_subject
-- ----------------------------
INSERT INTO `tb_subject` VALUES ('1', '数学');
INSERT INTO `tb_subject` VALUES ('2', '语文');
INSERT INTO `tb_subject` VALUES ('3', '英语');

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
  `userName` varchar(20) NOT NULL,
  `userPwd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES ('admin', 'root');
INSERT INTO `tb_user` VALUES ('teacher', '12345');

-- ----------------------------
-- View structure for v_classinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_classinfo`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_classinfo` AS select `tb_class`.`classID` AS `classID`,`tb_grade`.`gradeID` AS `gradeID`,`tb_grade`.`gradeName` AS `gradeName`,`tb_class`.`className` AS `className` from (`tb_class` join `tb_grade`) where (`tb_class`.`gradeID` = `tb_grade`.`gradeID`) ;

-- ----------------------------
-- View structure for v_resultinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_resultinfo`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_resultinfo` AS select `tb_result`.`ID` AS `ID`,`tb_result`.`stuID` AS `stuID`,`v_studentinfo`.`stuName` AS `stuName`,`tb_examkinds`.`kindName` AS `kindName`,`tb_subject`.`subName` AS `subName`,`v_studentinfo`.`className` AS `className`,`v_studentinfo`.`gradeName` AS `gradeName`,`tb_result`.`result` AS `result` from (((`tb_subject` join `tb_result`) join `tb_examkinds`) join `v_studentinfo`) where ((`tb_result`.`stuID` = `v_studentinfo`.`stuID`) and (`tb_result`.`kindID` = `tb_examkinds`.`kindID`) and (`tb_result`.`subID` = `tb_subject`.`subID`)) ;

-- ----------------------------
-- View structure for v_studentinfo
-- ----------------------------
DROP VIEW IF EXISTS `v_studentinfo`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_studentinfo` AS select `tb_student`.`stuID` AS `stuID`,`tb_student`.`stuName` AS `stuName`,`tb_student`.`age` AS `age`,`tb_student`.`sex` AS `sex`,`tb_student`.`phone` AS `phone`,`tb_student`.`address` AS `address`,`tb_class`.`className` AS `className`,`tb_grade`.`gradeName` AS `gradeName` from ((`tb_student` join `tb_class`) join `tb_grade`) where ((`tb_student`.`classID` = `tb_class`.`classID`) and (`tb_student`.`gradeID` = `tb_grade`.`gradeID`)) ;
