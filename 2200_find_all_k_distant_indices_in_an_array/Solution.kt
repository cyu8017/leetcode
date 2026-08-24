// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution {

    fun findKDistantIndices(nums: IntArray, key: Int, k: Int): MutableList<Int> {

            var n = nums.size
            var mark = BooleanArray(n)
            for (i in 0 until n) {
                if (nums[i] == key) {
                    var l = maxOf(0, i - k), r = minOf(n - 1, i + k)
                    for (j in l..r) { mark[j] = true }
                }
            }
            var ans = ArrayList<Int>()
            for (i in 0 until n) { if (mark[i]) ans.add(i) }
            return ans

    }

}
