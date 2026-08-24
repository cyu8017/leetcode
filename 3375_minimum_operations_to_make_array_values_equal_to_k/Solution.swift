// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var seen = Set<Int>()
        for x in nums {
            if x < k { return -1 }
            if x > k { seen.insert(x) }
        }
        return seen.count
    }
}
