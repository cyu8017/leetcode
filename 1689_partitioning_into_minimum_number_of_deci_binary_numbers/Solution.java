// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution {
    public int minPartitions(String n) {
        int best = 0;
        for (int i = 0; i < n.length(); i++) {
            best = Math.max(best, n.charAt(i) - '0');
        }
        return best;
    }
}
