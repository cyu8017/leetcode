// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

class Solution {
    fun sumDivisibleByK(nums: IntArray, k: Int): Int {
        var cnt = HashMap<Int, Int>()
        for (x in nums) { cnt.merge(x, 1, { a, b -> a + b }) }
        var ans = 0
        for (e in cnt) {
            if (e.value % k == 0) ans += e.key * e.value
        }
        return ans
    }
}
