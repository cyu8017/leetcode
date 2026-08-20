// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        if nums.count <= 4 { return 0 }
        let a = nums.sorted()
        var ans = Int.max
        for i in 0..<4 {
            ans = min(ans, a[a.count - 4 + i] - a[i])
        }
        return ans
    }
}
