// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/


class Solution {
    func maxTotalValue(_ nums: [Int], _ s: String) -> Int {
        let chars = Array(s)
        var answer = 0
        var i = 0
        while i < chars.count {
            if chars[i] == "0" { i += 1; continue }
            let start = i
            while i < chars.count && chars[i] == "1" { i += 1 }
            let end = i - 1
            if start == 0 {
                for index in start...end { answer += nums[index] }
                continue
            }
            var minimum = nums[start - 1]
            var total = 0
            for index in (start - 1)...end {
                total += nums[index]
                if nums[index] < minimum { minimum = nums[index] }
            }
            answer += total - minimum
        }
        return answer
    }
}
