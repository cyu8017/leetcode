// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

class Solution {
    public int partitionString(String s) {
        int ans = 1, seen = 0;
        for (char c : s) {
            int bit = 1 << (c - 'a');
            if ((seen & bit) != 0) {
                ans++;
                seen = 0;
            }
            seen |= bit;
        }
        return ans;
    }
}
