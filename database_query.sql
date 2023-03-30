-- Active: 1680094895485@@localhost@3306@User_info

CREATE TABLE  User_infSQ(
  user_name varchar(255) NOT NULL,
  Full_Name varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  getting_updates varchar(2) NOT NULL DEFAULT '0',
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM User_info.User_infSQ;

-- INSERT INTO User_infSQ (user_name, Full_Name, email, password)
-- VALUES ("shaqinair","Shaquille","shaqinair@gmail.com","123456");

