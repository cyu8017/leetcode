// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

object Solution {
  def minMovesToSeat(seats: Array[Int], students: Array[Int]): Int = {
    val a = seats.sorted
    val b = students.sorted
    var ans = 0
    var i = 0
    while (i < a.length) { ans += math.abs(a(i) - b(i)); i += 1 }
    ans
  }
}
