// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution {
    fun minMovesToSeat(seats: IntArray, students: IntArray): Int {
seats.sort()
students.sort()
var ans: Int = 0
for (i in 0 until seats.size) {
ans += kotlin.math.abs(seats[i] - students[i])
}
return ans
}
}
