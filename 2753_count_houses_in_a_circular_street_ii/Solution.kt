// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

class Solution {
    fun houseCount(street: IntArray, k: Int): Int {
        var n = street.size
        if (n == 0) return 0
        var start = -1
        for (i in 0 until n) {
            if (street[i] == 1) { start = i; break; }
        }
        if (start < 0) return 0
        var count = 1
        var moves = 0
        var i2 = start
        while (moves < k) {
            i2 = (i2 + 1) % n
            moves++
            if (i2 == start) break
            if (street[i2] == 1) count++
        }
        return count
    }
}
