// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

public class Solution {
    public int PartitionString(string s) {
        int ans = 1, seen = 0;
        foreach (char c in s) {
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
