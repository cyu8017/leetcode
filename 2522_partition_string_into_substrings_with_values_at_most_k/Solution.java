// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution {
    public int minimumPartition(String s, int k) {
        int ans = 1;
        long cur = 0;
        for (char ch : s.toCharArray()) {
            int d = ch - '0';
            if (d > k) return -1;
            long nxt = cur * 10 + d;
            if (nxt > k) {
                ans++;
                cur = d;
            } else {
                cur = nxt;
            }
        }
        return ans;
    }
}
