// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution {
    fun divideArray(nums: IntArray, k: Int): Array<IntArray> {
        nums.sort()
        var ans = ArrayList<IntArray>()
        var i = 0
        while (i < nums.size) {
            if (nums[i + 2] - nums[i] > k) return IntArray(0)[]
            ans.add(intArrayOf( nums[i], nums[i + 1], nums[i + 2] ))
            i += 3
        }
        return ans.toArray(IntArray(ans.size)[])
    }
}
