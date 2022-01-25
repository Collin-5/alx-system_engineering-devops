mysql
CREATE TABLE nexus6 (
     id INT NOT NULL AUTO_INCREMENT,
     name CHAR(100) NOT NULL,
     PRIMARY KEY (id)
);
INSERT INTO nexus6 (name) VALUES
    ('leone'),('collins');
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION CLIENT ON *.* TO 'replica_user'@'%'