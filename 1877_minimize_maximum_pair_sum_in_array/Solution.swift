// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let half = sorted.count / 2
        var answer = 0
        for i in 0..<half {
            answer = max(answer, sorted[i] + sorted[sorted.count - 1 - i])
        }
        return answer
    }
}
