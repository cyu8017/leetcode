// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

object Solution {
  def numRescueBoats(people: Array[Int], limit: Int): Int = {
    val arr = people.sorted
    var i = 0
    var j = arr.length - 1
    var boats = 0
    while (i <= j) {
      if (arr(i) + arr(j) <= limit) i += 1
      j -= 1
      boats += 1
    }
    boats
  }
}
