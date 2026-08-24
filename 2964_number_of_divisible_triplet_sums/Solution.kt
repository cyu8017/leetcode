// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

class Solution {
    fun divisibleTripletCount(nums: IntArray, d: Int): Int {
        var n = nums.size
        var ans = 0
        for (i in 0 until n) {
            var freq = HashMap<Int, Int>()
            for (j in i + 1 until n) {
                var need = (d - (nums[i] + nums[j]) % d) % d
                var f = freq.getOrDefault(need, 0)
                ans += f
                var key = nums[j] % d
                var f2 = freq.getOrDefault(key, 0)
                freq[key] = f2 + 1
            }
        }
        return ans
    }
}
