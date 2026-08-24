// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

class Solution {
    fun occurrencesOfElement(nums: IntArray, queries: IntArray, x: Int): IntArray {
        var ids = ArrayList<Int>()
        for (i in 0 until nums.size) { if (nums[i] == x) ids.add(i) }
        var ans = IntArray(queries.size)
        for (qi in 0 until queries.size) {
            var i = queries[qi]
            if (i - 1 < ids.size) ans[qi] = ids[i - 1]
            else ans[qi] = -1
        }
        return ans
    }
}
