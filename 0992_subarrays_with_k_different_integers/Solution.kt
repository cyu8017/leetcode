// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution {
    fun subarraysWithKDistinct(nums: IntArray, k: Int): Int {
return atMost(nums, k) - atMost(nums, k - 1)
}

    private fun atMost(nums: IntArray, m: Int): Int {
if (m < 0) {
return 0
}
var count: HashMap<Int, Int> = HashMap()
var left: Int = 0
var ans: Int = 0
for (right in 0 until nums.size) {
count.merge(nums[right], 1, { a, b -> a + b })
while (count.size > m) {
var v: Int = nums[left++]
if (count.merge(v, -1, { a, b -> a + b }) == 0) {
count.remove(v)
}
}
ans += right - left + 1
}
return ans
}
}
