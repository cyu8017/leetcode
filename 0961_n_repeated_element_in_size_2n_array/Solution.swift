// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution {
    func repeatedNTimes(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        for x in nums {
            if seen.contains(x) { return x }
            seen.insert(x)
        }
        return -1
    }
}
