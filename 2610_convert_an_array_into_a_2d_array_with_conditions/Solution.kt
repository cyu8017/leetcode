// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution {
    fun findMatrix(nums: IntArray): MutableList<MutableList<Int>> {
        var freq = HashMap<Int, Int>()
        var ans = ArrayList<MutableList<Int>>()
        for (x in nums) {
            var f = freq.getOrDefault(x, 0)
            if (f == ans.size) ans.add(ArrayList())
            ans[f].add(x)
            freq[x] = f + 1
        }
        return ans
    }
}
