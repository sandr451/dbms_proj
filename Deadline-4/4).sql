select o_id , avg_cost FROM (SELECT o_id , avg(cost)
FROM order_info
GROUP BY o_id) AS order_avg (O_ID,avg_cost)
WHERE avg_cost > 500 and avg_cost <3000