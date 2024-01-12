START TRANSACTION;

SELECT quantity_avl
FROM product
WHERE product_id = '123';


UPDATE quantity_avl
SET quantity_avl = quantity_avl -  731
WHERE product_id = '123';

INSERT INTO orders (Cust_ID, order_id) VALUES (29,301);
INSERT INTO order_info VALUES(o_id, p_id,seller_id,cost) VALUES (301,123,148,6729);

SELECT @product_quantity := quantity_avl FROM product WHERE product_id = '123';
IF @product_quantity = 0 THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;