// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

public class Solution {
    public long WonderfulSubstrings(string word) {
        var count = new long[1024];
        count[0] = 1;
        int mask = 0;
        long ans = 0;
        foreach (char ch in word) {
            mask ^= 1 << (ch - 'a');
            ans += count[mask];
            for (int bit = 0; bit < 10; bit++)
                ans += count[mask ^ (1 << bit)];
            count[mask]++;
        }
        return ans;
    }
}