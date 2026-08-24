// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution {

    fun countDistinct(nums: IntArray, k: Int, p: Int): Int {

            var n = nums.size
            var seen = HashSet<String>()
            for (i in 0 until n) {
                var div = 0
                var key = StringBuilder()
                for (j in i until n) {
                    if (nums[j] % p == 0) div++
                    if (div > k) break
                    key.append(nums[j] + 1).append(',')
                    seen.add(key.toString())
                }
            }
            return seen.size

    }

}
