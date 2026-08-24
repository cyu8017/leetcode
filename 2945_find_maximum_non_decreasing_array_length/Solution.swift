// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

class Solution {
    func findMaximumLength(_ nums: [Int]) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        var last = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        var dp = Array(repeating: 0, count: n + 1)
        var dq: [(Int, Int)] = [(0, 0)]
        for i in 1...n {
            while dq.count > 1 && dq[1].1 <= pref[i] { dq.removeFirst() }
            let j = dq[0].0
            dp[i] = dp[j] + 1
            last[i] = pref[i] - pref[j]
            let val = pref[i] + last[i]
            while !dq.isEmpty && dq.last!.1 >= val { dq.removeLast() }
            dq.append((i, val))
        }
        return dp[n]
    }
}
