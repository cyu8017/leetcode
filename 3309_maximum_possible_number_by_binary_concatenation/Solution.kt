// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution {
    private fun toBin(x: Int): String {
        if (x == 0) return "0"
        var s = StringBuilder()
        while (x > 0) {
            s.insert(0, (char) ('0' + (x and 1)))
            x = x shr 1
        }
        return s.toString()
    }

    fun maxGoodNumber(nums: IntArray): Int {
        var bs = arrayOfNulls<String>(3)
        for (i in 0 until 3) { bs[i] = toBin(nums[i]) }
        var idx = {0, 1, 2}
        var ans = {0}
        perm(0, idx, bs, ans)
        return ans[0]
    }

    private fun perm(i: Int, idx: IntArray, bs: Array<String>, ans: IntArray) {
        if (i == 3) {
            var s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
            var v = 0
            for (c in s.toCharArray()) { v = v * 2 + (c - '0') }
            if (v > ans[0]) ans[0] = v
            return
        }
        for (j in i until 3) {
            var t = idx[i]; idx[i] = idx[j]; idx[j] = t
            perm(i + 1, idx, bs, ans)
            t = idx[i]; idx[i] = idx[j]; idx[j] = t
        }
    }
}
