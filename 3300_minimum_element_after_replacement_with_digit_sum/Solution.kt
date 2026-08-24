// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution {
    fun minElement(nums: IntArray): Int {
        var ans = 1000000000
        for (num in nums) {
            var x = num
            var s = 0
            while (x > 0) { s += x % 10; x /= 10; }
            if (s < ans) ans = s
        }
        return ans
    }
}
