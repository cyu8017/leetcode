// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

using System.Linq;

public class Solution {
    public int MinPartitions(string n) {
        return n.Max(c => c - '0');
    }
}
