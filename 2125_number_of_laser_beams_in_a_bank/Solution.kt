// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution {
    fun numberOfBeams(bank: Array<String>): Int {
        var ans: Int = 0, prev = 0
        for (row in bank) {
            var cnt: Int = 0
            for (i in 0 until row.length) if (row[i] == '1') cnt++
            if (cnt > 0) {
                ans += prev * cnt
                prev = cnt
            }
        }
        return ans
    }
}
