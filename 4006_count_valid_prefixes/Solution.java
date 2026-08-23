// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

class Solution {
    public int countValidPrefixes(String s) {
        int ans = 0, t = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') t++;
            else t--;
            if (t >= -1 && t <= 1) ans++;
        }
        return ans;
    }
}
