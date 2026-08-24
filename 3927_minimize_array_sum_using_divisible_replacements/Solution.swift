// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/


class Solution {
    func minArraySum(_ nums: [Int]) -> Int {
        var maximum = 0
        var present = Array(repeating: false, count: 100001)
        for value in nums {
            present[value] = true
            if value > maximum { maximum = value }
        }
        var best = Array(repeating: 0, count: maximum + 1)
        for divisor in 1...max(1, maximum) {
            if divisor > maximum { break }
            if !present[divisor] { continue }
            var multiple = divisor
            while multiple <= maximum {
                if best[multiple] == 0 { best[multiple] = divisor }
                multiple += divisor
            }
        }
        var answer = 0
        for value in nums { answer += best[value] }
        return answer
    }
}
