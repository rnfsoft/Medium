DROP TABLE IF EXISTS features_group_2;

CREATE TABLE IF NOT EXISTS features_group_2 AS
SELECT 
  o1.index
  ,SUM(CASE WHEN o2.category = 1 then 1 else null end) AS category_1_count
  ,SUM(CASE WHEN o2.category = 2 then 1 else null end) AS category_2_count
  ,SUM(CASE WHEN o2.category = 3 then 1 else null end) AS category_3_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 1 then 1 else null end) AS event1_1_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 2 then 1 else null end) AS event1_2_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 4 then 1 else null end) AS event1_4_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 5 then 1 else null end) AS event1_5_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 6 then 1 else null end) AS event1_6_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 7 then 1 else null end) AS event1_7_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 8 then 1 else null end) AS event1_8_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 9 then 1 else null end) AS event1_9_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 10 then 1 else null end) AS event1_10_count
  ,SUM(CASE WHEN o2.event1 IS NOT NULL AND o2.event1 = 11 then 1 else null end) AS event1_11_count
  ,SUM(CASE WHEN o2.event1 IS NULL then 1 else null end) AS event1_null_count
  ,SUM(CASE WHEN o2.event2 = 1 then 1 else null end) AS event2_1_count
  ,SUM(CASE WHEN o2.event2 = 2 then 1 else null end) AS event2_2_count
  ,SUM(CASE WHEN o2.event2 = 3 then 1 else null end) AS event2_3_count
  ,SUM(CASE WHEN o2.event2 = 4 then 1 else null end) AS event2_4_count
  ,SUM(CASE WHEN o2.event2 = 5 then 1 else null end) AS event2_5_count
  ,SUM(CASE WHEN o2.event2 = 6 then 1 else null end) AS event2_6_count
  ,SUM(CASE WHEN o2.event2 = 7 then 1 else null end) AS event2_7_count
  ,SUM(CASE WHEN o2.event2 = 8 then 1 else null end) AS event2_8_count
  ,SUM(CASE WHEN o2.event2 = 9 then 1 else null end) AS event2_9_count
  ,SUM(CASE WHEN o2.event2 = 10 then 1 else null end) AS event2_10_count
FROM Online AS o1
JOIN Online AS o2
  ON o1.custno = o2.custno
  AND o1.dt >= o2.dt
GROUP BY o1.index;

CREATE INDEX ix_features_group_2_index ON features_group_2(index);

