// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution {
    func numberOfPoints(_ nums: [[Int]]) -> Int {
        var cov = Array(repeating: 0, count: 102)
        for r in nums {
            for x in r[0]...r[1] { cov[x] = 1 }
        }
        return cov.reduce(0, +)
    }
}
