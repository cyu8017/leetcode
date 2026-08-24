// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution {

    fun countHillValley(nums: IntArray): Int {

            var compact = ArrayList(Arrays.asList(nums[0] ))
            for (i in 1 until nums.size) { if (nums[i] != compact[compact.size - 1]) compact.add(nums[i]) }
            var ans = 0
            run { var i = 1; while (i + 1 < compact.size) { if ((compact[i] > compact[i - 1] && compact[i] > compact[i + 1]) ||
                    (compact[i] < compact[i - 1] && compact[i] < compact[i + 1]))
                    ans++; i++ } }
            return ans

    }

}
