// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution {
    func minPartitions(_ n: String) -> Int {
        n.compactMap { $0.wholeNumberValue }.max() ?? 0
    }
}
