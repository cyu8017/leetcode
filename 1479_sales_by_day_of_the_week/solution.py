QUERY = """SELECT item_category AS CATEGORY,
       SUM(CASE WHEN DAYOFWEEK(order_date)=2 THEN quantity ELSE 0 END) AS MONDAY,
       SUM(CASE WHEN DAYOFWEEK(order_date)=3 THEN quantity ELSE 0 END) AS TUESDAY,
       SUM(CASE WHEN DAYOFWEEK(order_date)=4 THEN quantity ELSE 0 END) AS WEDNESDAY,
       SUM(CASE WHEN DAYOFWEEK(order_date)=5 THEN quantity ELSE 0 END) AS THURSDAY,
       SUM(CASE WHEN DAYOFWEEK(order_date)=6 THEN quantity ELSE 0 END) AS FRIDAY,
       SUM(CASE WHEN DAYOFWEEK(order_date)=7 THEN quantity ELSE 0 END) AS SATURDAY,
       SUM(CASE WHEN DAYOFWEEK(order_date)=1 THEN quantity ELSE 0 END) AS SUNDAY
FROM Items i LEFT JOIN Orders o ON i.item_id=o.item_id
GROUP BY item_category ORDER BY item_category"""
