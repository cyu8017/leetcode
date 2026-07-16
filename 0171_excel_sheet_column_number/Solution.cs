public class Solution
{
    public int TitleToNumber(string columnTitle)
    {
        var result = 0;
        foreach (var ch in columnTitle)
        {
            result = result * 26 + (ch - 'A' + 1);
        }
        return result;
    }
}
