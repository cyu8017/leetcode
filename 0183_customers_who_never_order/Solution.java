class Solution {
    public static final String QUERY = """
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
)
""";
}
