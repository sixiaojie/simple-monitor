tee /tmp/temp.log
use zhang;
drop table if exists container_privilege;
create table `container_privilege`(
  `C_id` tinyint(4) NOT NULL,
                        `Name` varchar(20) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Privilege` char(2) not null,
  `Admin` char(1) not null,
  `Create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
alter table container_privilege add CONSTRAINT user_container_privilege FOREIGN KEY (C_id) REFERENCES container(C_id);
