// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

public class Solution {
    public IList<string> CellsInRange(string s) {
        var ans = new List<string>();
        for (char c = s[0]; c <= s[3]; c++)
            for (char r = s[1]; r <= s[4]; r++)
                ans.Add(new string(new[] { c, r }));
        return ans;
    }
}
