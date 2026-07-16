public class Solution {
    public const string QUERY = "\nDELETE p1\nFROM Person p1\nJOIN Person p2\n  ON p1.email = p2.email\n AND p1.id > p2.id\n";
}
