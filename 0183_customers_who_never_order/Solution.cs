public class Solution {
    public const string QUERY = @"
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
)
";
}
