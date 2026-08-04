// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution {
    public long wonderfulSubstrings(String word) {
        long[] count = new long[1024];
        count[0] = 1;
        int mask = 0;
        long ans = 0;
        for (int i = 0; i < word.length(); i++) {
            mask ^= 1 << (word.charAt(i) - 'a');
            ans += count[mask];
            for (int bit = 0; bit < 10; bit++) ans += count[mask ^ (1 << bit)];
            count[mask]++;
        }
        return ans;
    }
}
