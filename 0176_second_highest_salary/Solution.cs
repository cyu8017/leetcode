public class Solution
{
    public const string QUERY = "SELECT\n" +
        "    (\n" +
        "        SELECT DISTINCT salary\n" +
        "        FROM Employee\n" +
        "        ORDER BY salary DESC\n" +
        "        LIMIT 1 OFFSET 1\n" +
        "    ) AS SecondHighestSalary\n" +
        "";
}
