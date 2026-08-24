// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution {
    func numsSameConsecDiff(_ n: Int, _ k: Int) -> [Int] {
        var ans = [Int]()
        func dfs(_ num: Int, _ length: Int) {
            if length == n {
                ans.append(num)
                return
            }
            let last = num % 10
            var nexts = Set<Int>([last + k, last - k])
            for nxt in nexts where nxt >= 0 && nxt <= 9 {
                dfs(num * 10 + nxt, length + 1)
            }
        }
        for start in 1...9 { dfs(start, 1) }
        return ans
    }
}
