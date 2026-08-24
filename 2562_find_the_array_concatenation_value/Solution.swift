// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution {
    func findTheArrayConcVal(_ nums: [Int]) -> Int {
        var ans = 0
        var l = 0, r = nums.count - 1
        while l <= r {
            if l == r {
                ans += nums[l]
                break
            }
            let left = nums[l], right = nums[r]
            var pow = 1, t = right
            while t > 0 {
                pow *= 10
                t /= 10
            }
            ans += left * pow + right
            l += 1
            r -= 1
        }
        return ans
    }
}
