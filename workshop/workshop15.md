## Workshop15

1. 

```sql
CREATE TABLE bands(
	id int PRIMARY KEY,
    name text,
    debut int
    
);
```

```sql
INSERT INTO bands(id,name,debut) VALUES(1,"Queen",1973);
INSERT INTO bands(id,name,debut) VALUES(2,"Coldplay",1998);
INSERT INTO bands(id,name,debut) VALUES(1,"MCR",2001);
```



2.

```sql
SELECT id, name FROM bands
```



3.

```sql
SELECT name FROM bands WHERE dubut < 2000
```

