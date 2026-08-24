// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

class Solution {
    private lateinit var parent: IntArray

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    fun maxAlternatingSum(nums: IntArray, swaps: Array<IntArray>): Long {
        val n = nums.size
        parent = IntArray(n) { it }
        for (s in swaps) {
            val a = find(s[0])
            val b = find(s[1])
            if (a != b) parent[a] = b
        }
        val compVals = HashMap<Int, ArrayList<Int>>()
        val compIdx = HashMap<Int, ArrayList<Int>>()
        for (i in 0 until n) {
            val r = find(i)
            compVals.getOrPut(r) { ArrayList() }.add(nums[i])
            compIdx.getOrPut(r) { ArrayList() }.add(i)
        }
        val arr = IntArray(n)
        for ((r, vals) in compVals) {
            val idxs = compIdx[r]!!
            vals.sortDescending()
            val even = ArrayList<Int>()
            val odd = ArrayList<Int>()
            for (i in idxs) {
                if (i % 2 == 0) even.add(i) else odd.add(i)
            }
            even.sort()
            odd.sort()
            var ei = 0
            for (v in vals) {
                if (ei < even.size) {
                    arr[even[ei]] = v
                    ei++
                } else {
                    arr[odd[ei - even.size]] = v
                    ei++
                }
            }
        }
        var ans = 0L
        for (i in 0 until n) {
            if (i % 2 == 0) ans += arr[i]
            else ans -= arr[i]
        }
        return ans
    }
}
