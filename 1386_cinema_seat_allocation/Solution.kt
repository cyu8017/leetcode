// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

class Solution {
    fun maxNumberOfFamilies(n: Int, reservedSeats: Array<IntArray>): Int {
        val rows = mutableMapOf<Int, Int>()
        for (seat in reservedSeats) {
            val r = seat[0]
            val c = seat[1]
            if (c in 2..9) rows[r] = rows.getOrDefault(r, 0) or (1 shl (c - 2))
        }
        var ans = 2 * (n - rows.size)
        for (m in rows.values) {
            val left = (m and 0b00001111) == 0
            val right = (m and 0b11110000) == 0
            val middle = (m and 0b00111100) == 0
            ans += if (left && right) 2 else if (left || right || middle) 1 else 0
        }
        return ans
    }
}
