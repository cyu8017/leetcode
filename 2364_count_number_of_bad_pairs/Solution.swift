// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution {
    func countBadPairs(_ nums: [Int]) -> Int {
        let n = nums.count
        let total = n * (n - 1) / 2
        var freq: [Int: Int] = [:]
        var good = 0
        for i in 0..<n {
            let key = nums[i] - i
            good += freq[key, default: 0]
            freq[key, default: 0] += 1
        }
        return total - good
    }
}
