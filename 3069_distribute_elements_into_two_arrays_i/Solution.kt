// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution {
    fun resultArray(nums: IntArray): IntArray {
        var arr1 = ArrayList<Int>()
        var arr2 = ArrayList<Int>()
        arr1.add(nums[0])
        arr2.add(nums[1])
        for (i in 2 until nums.size) {
            if (arr1[arr1.size - 1] > arr2[arr2.size - 1]) arr1.add(nums[i])
            else arr2.add(nums[i])
        }
        arr1.addAll(arr2)
        var ans = IntArray(arr1.size)
        for (i in 0 until arr1.size) { ans[i] = arr1[i] }
        return ans
    }
}
