// LeetCode 1974 - Minimum Time to Type Word Using Special Typewriter
// https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution {
    public int minTimeToType(String word) {
        char cur = 'a';
        int ans = 0;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int d = Math.abs(ch - cur);
            ans += Math.min(d, 26 - d) + 1;
            cur = ch;
        }
        return ans;
    }
}
