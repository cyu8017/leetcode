// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

class Solution {
    public int countAsterisks(String s) {
        int ans = 0;
        boolean inside = false;
        for (char c : s) {
            if (c == '|') inside = !inside;
            else if (c == '*' && !inside) ans++;
        }
        return ans;
    }
}
