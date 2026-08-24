// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/


class Solution {
    func countGoodIntegers(_ l: Int, _ r: Int, _ k: Int) -> Int {
        return count(r, k) - count(l - 1, k)
    }

    private func count(_ bound: Int, _ k: Int) -> Int {
        if bound <= 0 { return 0 }
        let digits = Array(String(bound))
        var memo = [String: Int]()
        func dfs(_ position: Int, _ previous: Int, _ started: Bool, _ tight: Bool) -> Int {
            if position == digits.count { return started ? 1 : 0 }
            let key = "\(position),\(previous),\(started)"
            if !tight, let v = memo[key] { return v }
            let limit = tight ? Int(String(digits[position]))! : 9
            var result = 0
            for digit in 0...limit {
                let nextStarted = started || digit != 0
                if started && abs(previous - digit) > k { continue }
                let nextPrevious = nextStarted ? digit : previous
                result += dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit)
            }
            if !tight { memo[key] = result }
            return result
        }
        return dfs(0, 0, false, true)
    }
}
