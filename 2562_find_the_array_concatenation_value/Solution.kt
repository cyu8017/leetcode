// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution {
    fun findTheArrayConcVal(nums: IntArray): Long {
        var ans = 0
        var l = 0
        var r = nums.size - 1
        while (l <= r) {
            if (l == r) {
                ans += nums[l]
                break
            }
            var left = nums[l]
            var right = nums[r]
            var pow = 1
            run {
                var t = right
                while (t > 0) {
                    pow *= 10
                    t /= 10
                }
            }
            ans += left * pow + right
            l = l + 1
            r = r - 1
        }
        return ans
    }
}
