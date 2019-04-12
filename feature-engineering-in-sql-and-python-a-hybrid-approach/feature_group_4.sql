DROP TABLE IF EXISTS features_group_4;

CREATE TABLE IF NOT EXISTS features_group_4 AS
SELECT
  off_set.index
  ,p3.revenue AS last_revenue
  ,p3.prodcat1 AS last_prodcat1
  ,p3.prodcat2 AS last_prodcat2
FROM
(SELECT 
  o1.index
  ,o1.custno
  ,MAX(p2.orderdate) AS last_dt
FROM Online AS o1
JOIN Purchase AS p2
  ON o1.custno = p2.custno
  AND o1.dt > p2.orderdate
GROUP BY o1.index, o1.custno) AS off_set
JOIN Purchase AS p3
ON off_set.custno = p3.custno
AND off_set.last_dt = p3.orderdate;

CREATE INDEX ix_features_group_4_index ON features_group_4(index);