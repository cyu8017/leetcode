public class Solution {
    public const string QUERY = "\nSELECT w1.id\nFROM Weather w1\nJOIN Weather w2\n  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1\nWHERE w1.temperature > w2.temperature\n";
}
