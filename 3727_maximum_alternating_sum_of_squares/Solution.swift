// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution {
    func maxAlternatingSum(_ nums: [Int]) -> Int {
        var a = nums.map { $0 * $0 }
        a.sort()
        let m = a.count / 2
        var ans = 0
        for i in 0..<m { ans -= a[i] }
        for i in m..<a.count { ans += a[i] }
        return ans
    }
}
