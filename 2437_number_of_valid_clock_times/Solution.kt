// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

class Solution {
    fun countTime(time: String): Int {
        var ans = 0
        for (h in 0 until 24) {
            for (m in 0 until 60) {
                val h0 = ('0'.code + h / 10).toChar()
                val h1 = ('0'.code + h % 10).toChar()
                val m0 = ('0'.code + m / 10).toChar()
                val m1 = ('0'.code + m % 10).toChar()
                if (time[0] != '?' && time[0] != h0) continue
                if (time[1] != '?' && time[1] != h1) continue
                if (time[3] != '?' && time[3] != m0) continue
                if (time[4] != '?' && time[4] != m1) continue
                ans++
            }
        }
        return ans
    }
}
