// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

class Solution {
    fun countPairs(nums: IntArray): Int {
        var ans = 0
        for (i in nums.indices) {
            for (j in i + 1 until nums.size) {
                if (almostEqual(nums[i], nums[j])) ans++
            }
        }
        return ans
    }

    private fun sprintfNum(x0: Int): String {
        var x = x0
        if (x == 0) return "0"
        val b = StringBuilder()
        while (x > 0) {
            b.insert(0, ('0'.code + x % 10).toChar())
            x /= 10
        }
        return b.toString()
    }

    private fun almostEqual(a: Int, b: Int): Boolean {
        var sa = sprintfNum(a)
        var sb = sprintfNum(b)
        while (sa.length < sb.length) sa = "0$sa"
        while (sb.length < sa.length) sb = "0$sb"
        val diff = ArrayList<Int>()
        for (i in sa.indices) {
            if (sa[i] != sb[i]) diff.add(i)
        }
        if (diff.isEmpty()) return true
        if (diff.size != 2) return false
        val i0 = diff[0]
        val j = diff[1]
        return sa[i0] == sb[j] && sa[j] == sb[i0]
    }
}
