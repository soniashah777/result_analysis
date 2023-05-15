use resultdb;
create table xiiresult (sname varchar (100) primary key,english floAT,fmm FLOAT, hindi float, math float,ped int, acc float, ai float, bio float, phy float, chem float, eco float, bst float, cs float );
create table xresult (sname varchar (100) primary key,mathb float, hindi float, math float,sci float,sst float,ca float, english floAT,fmm float, ai float);
select * from xresult;
delete from xresult where sname like " ABDUS SAMI QAZI";
INSERT INTO xresult(sname, hindi,english,math,sci,sst,ai) VALUES (086, 086, 043, 077, 093,085);