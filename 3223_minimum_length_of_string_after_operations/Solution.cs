// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

public class Solution {
    public int MinimumLength(string s) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        int ans = 0;
        foreach (int x in cnt) {
            if (x > 0) ans += (x & 1) != 0 ? 1 : 2;
        }
        return ans;
    }
}
