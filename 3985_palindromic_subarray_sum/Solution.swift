// LeetCode 3985 - Palindromic Subarray Sum
// https://leetcode.com/problems/palindromic-subarray-sum/


class Solution {
    func maxPalindromicSubarraySum(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + nums[i] }
        var odd = Array(repeating: 0, count: n)
        var left = 0, right = -1
        for i in 0..<n {
            var radius = 1
            if i <= right {
                let mirror = left + right - i
                radius = odd[mirror]
                if right - i + 1 < radius { radius = right - i + 1 }
            }
            while i - radius >= 0 && i + radius < n && nums[i - radius] == nums[i + radius] {
                radius += 1
            }
            odd[i] = radius
            if i + radius - 1 > right {
                left = i - radius + 1
                right = i + radius - 1
            }
        }
        var even = Array(repeating: 0, count: n)
        left = 0; right = -1
        for i in 0..<n {
            var radius = 0
            if i <= right {
                let mirror = left + right - i + 1
                radius = even[mirror]
                if right - i + 1 < radius { radius = right - i + 1 }
            }
            while i - radius - 1 >= 0 && i + radius < n && nums[i - radius - 1] == nums[i + radius] {
                radius += 1
            }
            even[i] = radius
            if i + radius - 1 > right {
                left = i - radius
                right = i + radius - 1
            }
        }
        var answer = 0
        for i in 0..<n {
            var sum = prefix[i + odd[i]] - prefix[i - odd[i] + 1]
            if sum > answer { answer = sum }
            if even[i] > 0 {
                sum = prefix[i + even[i]] - prefix[i - even[i]]
                if sum > answer { answer = sum }
            }
        }
        return answer
    }
}
