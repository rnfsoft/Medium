DROP TABLE IF EXISTS features_group_3;

CREATE TABLE IF NOT EXISTS features_group_3 AS
SELECT
  off_set.index
  ,o3.category AS last_category
  ,o3.event1 AS last_event1
  ,o3.event2 AS last_event2
FROM
(SELECT 
  o1.index
  ,o1.custno
  ,MAX(o2.dt) AS last_dt
FROM online AS o1
JOIN online AS o2
  ON o1.custno = o2.custno
  AND o1.dt > o2.dt
GROUP BY o1.index, o1.custno) AS off_set
JOIN online AS o3
ON off_set.custno = o3.custno
AND off_set.last_dt = o3.dt;

CREATE INDEX ix_features_group_3_index ON features_group_3(index);
