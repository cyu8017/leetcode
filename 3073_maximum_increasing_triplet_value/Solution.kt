// LeetCode 3073 - Maximum Increasing Triplet Value
// https://leetcode.com/problems/maximum-increasing-triplet-value/

class Solution {
    fun maximumTripletValue(nums: IntArray): Int {
        var n = nums.size
        var right = IntArray(n)
        right[n - 1] = nums[n - 1]
        run {
            var i = n - 2
            while (i >= 0) {
                right[i] = maxOf(nums[i], right[i + 1])
                i--
            }
        }
        var ts = TreeSet<Int>()
        ts.add(nums[0])
        var ans = 0
        for (j in 1 until n - 1) {
            if (right[j + 1] > nums[j]) {
                var it = ts.lower(nums[j])
                if (it != null) ans = maxOf(ans, it - nums[j] + right[j + 1])
            }
            ts.add(nums[j])
        }
        return ans
    }
}
