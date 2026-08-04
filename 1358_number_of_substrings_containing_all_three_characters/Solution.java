// LeetCode 1358 - Number Of SubStrings Containing All Three Characters
// https://leetcode.com/problems/number-of-subStrings-containing-all-three-characters/

class Solution {
    public int numberOfSubStrings(String s) {
        int[] last = { -1, -1, -1 }; int ans = 0;
        for (int i = 0; i < s.length; i++) {
            last[s[i] - 'a'] = i;
            ans += Math.min(last[0], Math.min(last[1], last[2])) + 1;
        }
        return ans;
    }
}
