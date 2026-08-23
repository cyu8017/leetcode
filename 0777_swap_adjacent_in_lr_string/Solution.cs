// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

using System.Text;

public class Solution {
    public bool CanTransform(string start, string result) {
        var a = new StringBuilder();
        var b = new StringBuilder();
        foreach (char ch in start) if (ch != 'X') a.Append(ch);
        foreach (char ch in result) if (ch != 'X') b.Append(ch);
        if (a.ToString() != b.ToString()) return false;
        int i = 0, j = 0, n = start.Length;
        while (i < n && j < n) {
            while (i < n && start[i] == 'X') i++;
            while (j < n && result[j] == 'X') j++;
            if (i == n || j == n) break;
            if (start[i] != result[j]) return false;
            if (start[i] == 'L' && i < j) return false;
            if (start[i] == 'R' && i > j) return false;
            i++;
            j++;
        }
        return true;
    }
}
