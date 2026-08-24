// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution {
    func findMaxK(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        var ans = -1
        for x in nums {
            seen.insert(x)
            if x > 0 && seen.contains(-x) && x > ans { ans = x }
            if x < 0 && seen.contains(-x) && -x > ans { ans = -x }
        }
        return ans
    }
}
