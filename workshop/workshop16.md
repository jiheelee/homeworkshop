### WORKSHOP 16



#### 1. 해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라.

```sql
ALTER TABLE bands ADD members INTEGER;

INSERT INTO bands(members) VALUES(4) WHERE id=1;
INSERT INTO bands(members) VALUES(5) WHERE id=2;
INSERT INTO bands(members) VALUES(9) WHERE id=3;

```



#### 2.  Id 가 3인 레코드의 members 를 5로 수정하라.

```sql
UPDATE bands set members=5 WHERE id=3;
```



#### 3. Id 가 2인 레코드를 삭제하라

```sql
DELETE FROM bands WHERE id=2;
```



