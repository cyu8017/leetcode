// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

public class Solution {
    public int CountAsterisks(string s) {
        int ans = 0;
        bool inside = false;
        foreach (char c in s) {
            if (c == '|') inside = !inside;
            else if (c == '*' && !inside) ans++;
        }
        return ans;
    }
}
