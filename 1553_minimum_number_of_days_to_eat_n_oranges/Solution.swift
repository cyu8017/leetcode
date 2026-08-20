// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

class Solution {
    func minDays(_ n: Int) -> Int {
        var memo = [Int: Int]()
        func dp(_ x: Int) -> Int {
            if x <= 1 { return x }
            if let v = memo[x] { return v }
            let ans = 1 + min(x % 2 + dp(x / 2), x % 3 + dp(x / 3))
            memo[x] = ans
            return ans
        }
        return dp(n)
    }
}
