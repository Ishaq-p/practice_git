-- Active: 1680094895485@@localhost@3306@User_info

CREATE TABLE  User_infSQ(
  user_name varchar(255) NOT NULL,
  Full_Name varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  password_ varchar(255) NOT NULL,
  getting_updates varchar(2) NOT NULL DEFAULT '0',
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM User_info.User_infSQ;

-- INSERT INTO User_infSQ (user_name, Full_Name, email, password)
-- VALUES ("shaqinair","Shaquille","shaqinair@gmail.com","123456");

SELECT Full_Name FROM User_info.User_infSQ WHERE user_name = "emirkhan";

SELECT user_name FROM User_info.User_infSQ WHERE user_name = "emirkhan";

SELECT user_name FROM User_info.User_infSQ WHERE email = "shaqinair@gmail.com";


SELECT * FROM User_info.User_infSQ WHERE user_name = 'ishaqpaktin';

UPDATE User_infSQ1
SET password_ = 'abdelghafar'
WHERE user_name = 'emirkhan'; 

SELECT * FROM User_infSQ1;

INSERT INTO User_infSQ1 (user_name, Full_Name, email, password_) VALUES ("emirkhan","Emir","KHAN@GMAIL.COM", "khanzaman**99");


SELECT * FROM User_infSQ;