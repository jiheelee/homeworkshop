#### 1. 다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.

```sql
CREATE TABLE friends(
	id INT,
    name TEXT,
    location TEXT
);
```



#### 2. 해당 테이블에 다음과 같이 데이터를 입력한다.

```sql
INSERT INTO friends(id, name, location) VALUES(1,Justin, Seoul);
INSERT INTO friends(id, name, location) VALUES(2,Simon, New Work);
INSERT INTO friends(id, name, location) VALUES(3,Chang, Las Vegas);
INSERT INTO friends(id, name, location) VALUES(4,John, Sydney);
```



#### 3. 

```sql
ALTER TABLE friends ADD COLUMN married INT;
```



4.

```sql
UPDATE friends SET married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;
UPDATE friends SET married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;
```



5.

```sql
DELETE FROM friends WHERE married=0;
```

