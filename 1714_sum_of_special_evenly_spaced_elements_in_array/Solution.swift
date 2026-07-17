// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

class Solution {
    func solve(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let mod = 1000000007
        let n = nums.count
        let block = Int(Double(n).squareRoot()) + 1
        var dp = [[Int]](repeating: [Int](repeating: 0, count: n), count: block)
        for step in 1..<block {
            for i in stride(from: n - 1, through: 0, by: -1) {
                let next = i + step < n ? dp[step][i + step] : 0
                dp[step][i] = (nums[i] + next) % mod
            }
        }
        var ans = [Int]()
        ans.reserveCapacity(queries.count)
        for query in queries {
            let start = query[0]
            let step = query[1]
            if step < block {
                ans.append(dp[step][start])
            } else {
                var total = 0
                var i = start
                while i < n {
                    total += nums[i]
                    i += step
                }
                ans.append(total % mod)
            }
        }
        return ans
    }
}
