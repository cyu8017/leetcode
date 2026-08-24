// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

class Solution {
    private lateinit var nums: IntArray
    private lateinit var changeIndices: IntArray
    private var n = 0

    private fun ok(t: Int): Boolean {
        val last = IntArray(n + 1)
        for (s in 0 until t) last[changeIndices[s]] = s
        var decrement = 0; var marked = 0
        for (s in 0 until t) {
            val i = changeIndices[s]
            if (last[i] == s) {
                if (decrement < nums[i - 1]) return false
                decrement -= nums[i - 1]; marked++
            } else decrement++
        }
        return marked == n
    }

    fun earliestSecondToMarkIndices(nums: IntArray, changeIndices: IntArray): Int {
        this.nums = nums; this.changeIndices = changeIndices; this.n = nums.size
        val m = changeIndices.size
        var l = 0; var r = m + 1
        while (l < r) {
            val mid = (l + r) / 2
            if (ok(mid)) r = mid else l = mid + 1
        }
        return if (l > m) -1 else l
    }
}
