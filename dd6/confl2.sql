START TRANSACTION;

DELETE FROM orders
WHERE order_id = '5';

INSERT INTO ret_rep_requests (o_id, adm,product,del_per,req_iq) VALUES (5,22,500,5,101);

COMMIT;