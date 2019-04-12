-- Converted MySQL to Postgres 
DROP TABLE IF EXISTS features_group_1;

CREATE TABLE IF NOT EXISTS features_group_1 AS

SELECT o.index
  ,LEFT(o.dt, 10) AS day
  ,COUNT(*) AS order_count
  ,SUM(p.revenue) AS revenue_sum
  ,MAX(p.revenue) AS revenue_max
  ,MIN(p.revenue) AS revenue_min
  ,SUM(p.revenue) / COUNT(*) AS rev_p_order
  ,COUNT(p.prodcat1) AS prodcat1_count
  ,COUNT(p.prodcat2) AS prodcat2_count
  ,DATE_PART('days', MAX(p.orderdate)::date) - DATE_PART('days', o.dt::date) AS days_last_order
  ,DATE_PART('days', MAX(CASE WHEN p.prodcat1 IS NOT NULL THEN p.orderdate ELSE NULL END)::date) - DATE_PART('days', o.dt::date) AS days_last_prodcat1
  ,DATE_PART('days', MAX(CASE WHEN p.prodcat2 IS NOT NULL THEN p.orderdate ELSE NULL END)::date) - DATE_PART('days', o.dt::date) AS days_last_prodcat2
  ,SUM(CASE WHEN p.prodcat1=1 then 1 else null end) AS prodcat1_1_count
  ,SUM(CASE WHEN p.prodcat1=2 then 1 else null end) AS prodcat1_2_count
  ,SUM(CASE WHEN p.prodcat1=3 then 1 else null end) AS prodcat1_3_count
  ,SUM(CASE WHEN p.prodcat1=4 then 1 else null end) AS prodcat1_4_count
  ,SUM(CASE WHEN p.prodcat1=5 then 1 else null end) AS prodcat1_5_count
  ,SUM(CASE WHEN p.prodcat1=6 then 1 else null end) AS prodcat1_6_count
  ,SUM(CASE WHEN p.prodcat1=7 then 1 else null end) AS prodcat1_7_count
FROM online AS o 
JOIN purchase AS p
  ON o.custno = p.custno
  AND p.orderdate <= o.dt
GROUP BY 
o.dt,
o.index;

CREATE INDEX ix_features_group_1_index ON features_group_1(index);
