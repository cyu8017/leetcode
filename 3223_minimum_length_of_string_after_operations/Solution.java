// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution {
    public int minimumLength(String s) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) cnt[s.charAt(i) - 'a']++;
        int ans = 0;
        for (int x : cnt) {
            if (x > 0) ans += (x & 1) != 0 ? 1 : 2;
        }
        return ans;
    }
}
