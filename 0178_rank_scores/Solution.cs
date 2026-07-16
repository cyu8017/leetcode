public class Solution
{
    public const string QUERY = "SELECT\n" +
        "    score,\n" +
        "    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`\n" +
        "FROM Scores\n" +
        "ORDER BY score DESC\n" +
        "";
}
