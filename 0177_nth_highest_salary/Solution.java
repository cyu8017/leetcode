public class Solution {
    public static final String QUERY = "CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT\n" +
        "BEGIN\n" +
        "  DECLARE M INT;\n" +
        "  SET M = N - 1;\n" +
        "  RETURN (\n" +
        "    SELECT DISTINCT salary\n" +
        "    FROM Employee\n" +
        "    ORDER BY salary DESC\n" +
        "    LIMIT 1 OFFSET M\n" +
        "  );\n" +
        "END\n" +
        "";
}
