// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

class Solution {
    func leastOpsExpressTarget(_ x: Int, _ target: Int) -> Int {
        var memo = [Int: Int]()
        func dfs(_ t: Int) -> Int {
            if let v = memo[t] { return v }
            if x > t {
                let ans = min(2 * t - 1, 2 * (x - t))
                memo[t] = ans
                return ans
            }
            if x == t {
                memo[t] = 0
                return 0
            }
            var prod = x
            var n = 0
            while prod < t {
                prod *= x
                n += 1
            }
            if prod == t {
                memo[t] = n
                return n
            }
            var ans = dfs(t - prod / x) + n
            if prod < 2 * t { ans = min(ans, dfs(prod - t) + n + 1) }
            memo[t] = ans
            return ans
        }
        return dfs(target)
    }
}
