SELECT * FROM dojos_and_ninjas.ninjas;
SET SQL_SAFE_UPDATES = 0;


select * from ninjas;
insert into ninjas (first_name,last_name,age,dojo_id)
 values ("iheb","benslimen",28,4),("houssem","bahri",27,4),("sadok","zrelli",25,4);
 
 insert into ninjas (first_name,last_name,age,dojo_id)
 values ("nejah","dahmeni",22,5),("alex","smith",20,5),("jack","bell",30,5);
 
 insert into ninjas (first_name,last_name,age,dojo_id)
 values ("lil","wayne",18,6),("lasmer","samara",27,6),("ali","gezgez",30,6);
 
 DELETE FROM ninjas WHERE first_name = "sadok" or "houssem" = first_name or first_name = "iheb";
 delete from ninjas where id = 13 or id = 14 or id = 15;
 
 select * from ninjas order by id;
 
 select n.* , d.* from ninjas n join dojos d where n.dojo_id  = d.id and n.id = 11
 
 