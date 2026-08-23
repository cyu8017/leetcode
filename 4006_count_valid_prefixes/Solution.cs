// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

public class Solution {
    public int CountValidPrefixes(string s) {
        int ans = 0, t = 0;
        foreach (char c in s) {
            if (c == '1') t++;
            else t--;
            if (t >= -1 && t <= 1) ans++;
        }
        return ans;
    }
}
