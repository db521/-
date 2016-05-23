#发布需求---订单名称和需求描述
SELECT * FROM keeper_order_requirement WHERE order_id=61
#发布需求---附件
SELECT * FROM order_attachment WHERE order_id=61
#订单
TRUNCATE TABLE 
SELECT * FROM t_order WHERE order_number=60534
#确认初稿----设计稿名称及方案描述
SELECT * FROM order_solution WHERE order_id=23
#方案附件路径
SELECT * FROM order_solution_attachment WHERE order_solution_id IN(SELECT id FROM order_solution WHERE order_id=177)
UPDATE order_solution_attachment SET watermark_path="" WHERE order_solution_id IN(SELECT id FROM order_solution WHERE order_id=177)
#方案分类描述
SELECT * FROM solution_type WHERE solution_id IN (SELECT id FROM order_solution WHERE order_id=177)
#源文件路径
SELECT * FROM order_final_solution WHERE order_id=61
#用户信息
SELECT * FROM USER WHERE phone=18577777777
#用户个人资料
SELECT * FROM user_customer WHERE user_id IN(SELECT id FROM daodao.user WHERE phone=18577777777)
#管家个人资料
SELECT * FROM user_keeper WHERE user_id IN(SELECT id FROM daodao.user WHERE phone=18577777777)
