// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

class Solution {
    private lateinit var sa: String
    private lateinit var sb: String

    fun countPairs(nums: IntArray): Int {
        var ans = 0
        for (i in nums.indices) {
            for (j in i + 1 until nums.size) {
                if (almostEqual(nums[i], nums[j])) ans++
            }
        }
        return ans
    }

    private fun padNum(x0: Int): String {
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
        sa = padNum(a)
        sb = padNum(b)
        while (sa.length < sb.length) sa = "0$sa"
        while (sb.length < sa.length) sb = "0$sb"
        if (sa == sb) return true
        return canWithSwaps(2)
    }

    private fun canWithSwaps(maxSwap: Int): Boolean {
        val arr = sa.toCharArray()
        return dfs(arr, 0, maxSwap)
    }

    private fun dfs(arr: CharArray, start: Int, left: Int): Boolean {
        if (String(arr) == sb) return true
        if (left == 0) return false
        for (i in start until arr.size) {
            if (arr[i] == sb[i]) continue
            for (j in i + 1 until arr.size) {
                if (arr[j] == sb[i]) {
                    val tmp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = tmp
                    if (dfs(arr, i + 1, left - 1)) return true
                    val tmp2 = arr[i]
                    arr[i] = arr[j]
                    arr[j] = tmp2
                }
            }
            return false
        }
        return String(arr) == sb
    }
}
