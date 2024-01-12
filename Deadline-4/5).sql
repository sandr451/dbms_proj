select a.o_id , a.p_id, a.cost 
from order_info a 
JOIN order_info b 
ON a.p_id=b.p_id