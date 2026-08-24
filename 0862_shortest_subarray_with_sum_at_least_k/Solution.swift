// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution {
    func shortestSubarray(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        var dq = [Int]()
        var ans = n + 1
        for i in 0...n {
            while !dq.isEmpty && prefix[i] - prefix[dq[0]] >= k {
                ans = min(ans, i - dq.removeFirst())
            }
            while !dq.isEmpty && prefix[i] <= prefix[dq.last!] { dq.removeLast() }
            dq.append(i)
        }
        return ans <= n ? ans : -1
    }
}
