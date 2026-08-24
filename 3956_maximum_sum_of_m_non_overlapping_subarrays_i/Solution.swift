// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/


class Solution {
    func maxSum(_ nums: [Int], _ m: Int, _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        var dp = Array(repeating: 0, count: n + 1)
        var bestSelected = -(Int.max / 4)
        for _ in 1...m {
            var next = dp
            var deque = [Int]()
            for end in 1...n {
                let addIndex = end - l
                if addIndex >= 0 {
                    let value = dp[addIndex] - prefix[addIndex]
                    while !deque.isEmpty {
                        let last = deque[deque.count - 1]
                        if dp[last] - prefix[last] > value { break }
                        deque.removeLast()
                    }
                    deque.append(addIndex)
                }
                let minIndex = end - r
                while !deque.isEmpty && deque[0] < minIndex { deque.removeFirst() }
                if !deque.isEmpty {
                    let candidate = prefix[end] + dp[deque[0]] - prefix[deque[0]]
                    if candidate > next[end] { next[end] = candidate }
                    if candidate > bestSelected { bestSelected = candidate }
                }
                if next[end - 1] > next[end] { next[end] = next[end - 1] }
            }
            dp = next
        }
        return bestSelected
    }
}
