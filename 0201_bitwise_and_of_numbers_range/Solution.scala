// LeetCode 0201 - Bitwise AND of Numbers Range\n// https://leetcode.com/problems/\n\nobject Solution {
  def rangeBitwiseAnd(left: Int, right: Int): Int = {
    var low = left
    var high = right
    var shift = 0
    while (low < high) { low >>= 1; high >>= 1; shift += 1 }
    low << shift
  }
}
