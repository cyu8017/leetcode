// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution {
    fun averageValue(nums: IntArray): Int {
            var sum: Int = 0
            var cnt: Int = 0
            for (x in nums) {
                if (x % 6 == 0) {
                    sum +=x
                    cnt = cnt + 1
                }
            }
            return if (cnt == 0) 0 else sum / cnt
    }
}
