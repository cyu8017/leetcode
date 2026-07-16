# How We Solve Customers Who Bought All Products

Group purchases by customer and require the distinct product count to equal the total number of products.

## Steps

1. Count distinct `product_key` values per `customer_id`.
2. Compare that count to `(SELECT COUNT(*) FROM Product)`.
3. Return customers whose counts match.
