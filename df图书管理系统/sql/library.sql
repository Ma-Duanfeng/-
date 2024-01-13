-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2024-01-07 13:27:41
-- 服务器版本： 8.0.12
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `library`
--

-- --------------------------------------------------------

--
-- 表的结构 `admin`
--

CREATE TABLE `admin` (
  `管理员账号` varchar(8) NOT NULL,
  `姓名` varchar(255) NOT NULL,
  `密码` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `admin`
--

INSERT INTO `admin` (`管理员账号`, `姓名`, `密码`) VALUES
('200511', 'Rose', '0042019'),
('201912', 'Amanda', '0022022'),
('202001', 'Alice', '0012023'),
('202306', 'Peter', '0032022');

-- --------------------------------------------------------

--
-- 表的结构 `book`
--

CREATE TABLE `book` (
  `书号` char(8) NOT NULL,
  `类别` varchar(45) DEFAULT NULL,
  `书名` varchar(45) DEFAULT NULL,
  `出版社` varchar(45) DEFAULT NULL,
  `出版年份` int(11) DEFAULT NULL,
  `作者` varchar(45) DEFAULT NULL,
  `价格` float DEFAULT NULL,
  `在馆册数` int(11) DEFAULT NULL,
  `馆藏册数` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `book`
--

INSERT INTO `book` (`书号`, `类别`, `书名`, `出版社`, `出版年份`, `作者`, `价格`, `在馆册数`, `馆藏册数`) VALUES
('A0001', '马克思主义、列宁主义、毛泽东思想、邓小平理论', '学经典悟原理', '人民出版社', 2022, '孙经国', 61.08, 0, 2),
('A0002', '马克思主义、列宁主义、毛泽东思想、邓小平理论', '真理的力量（马克思主义为什么行）', '人民日报', 2023, '徐国亮', 49, 2, 2),
('A0003', '马克思主义、列宁主义、毛泽东思想、邓小平理论', '公正与人权（国外马克思主义研究以及价值与局限）', '南开大学出版社', 2023, '冯颜利', 128, 0, 3),
('A0004', '马克思主义、列宁主义、毛泽东思想、邓小平理论', '马克思的朋友圈', '人民出版社', 2023, '龚云', 88, 10, 14),
('B0001', '哲学、宗教', '佛说大乘无量寿庄严清净平等觉经', '不详', 2009, '不详', 0, 1, 1),
('B0002', '哲学、宗教', '参赞化育(惠栋易学考古中的大道微言)', '三联书店出版社', 2024, '古继明', 99, 0, 0),
('B0003', '哲学、宗教', '如何工作：松下幸之助谈快速成为好员工的心得', '人民东方出版社', 2024, '松下幸之助', 54, 0, 0),
('B0004', '哲学、宗教', '情绪瓶子', '海豚出版社', 2023, ' (英) 汤姆·布拉辛顿', 55, 15, 27);

-- --------------------------------------------------------

--
-- 表的结构 `card`
--

CREATE TABLE `card` (
  `账号` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `姓名` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `性别` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `人员类别` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `单位` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `密码` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `card`
--

INSERT INTO `card` (`账号`, `姓名`, `性别`, `人员类别`, `单位`, `密码`) VALUES
('3220100001', '刘涛', '女', '学生', '公共管理学院', '0001'),
('3235810', '徐海', '男', '教师', '创新创业学院', '5810');

-- --------------------------------------------------------

--
-- 表的结构 `record`
--

CREATE TABLE `record` (
  `书号` varchar(8) DEFAULT NULL,
  `卡号` varchar(10) DEFAULT NULL,
  `借书日期` datetime DEFAULT NULL,
  `还书日期` datetime DEFAULT NULL,
  `经手人` varchar(8) DEFAULT NULL,
  `状态` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `record`
--

INSERT INTO `record` (`书号`, `卡号`, `借书日期`, `还书日期`, `经手人`, `状态`) VALUES
('A0001', '3220100001', '2024-01-07 00:00:00', NULL, NULL, 10),
('A0001', '', NULL, '2024-01-07 00:00:00', NULL, 10),
('A0003', '3235810', '2024-01-07 00:00:00', NULL, NULL, 10);

--
-- 转储表的索引
--

--
-- 表的索引 `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`管理员账号`);

--
-- 表的索引 `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`书号`);

--
-- 表的索引 `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`账号`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
