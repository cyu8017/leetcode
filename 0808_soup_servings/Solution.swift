// LeetCode 0808 - Soup Servings
// https://leetcode.com/problems/soup-servings/

class Solution {
    func soupServings(_ n: Int) -> Double {
        if n >= 4800 { return 1.0 }
        let units = (n + 24) / 25
        var memo = [Int: Double]()
        func dp(_ a: Int, _ b: Int) -> Double {
            if a <= 0 && b <= 0 { return 0.5 }
            if a <= 0 { return 1.0 }
            if b <= 0 { return 0.0 }
            let key = (a << 16) | b
            if let v = memo[key] { return v }
            let val = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))
            memo[key] = val
            return val
        }
        return dp(units, units)
    }
}
