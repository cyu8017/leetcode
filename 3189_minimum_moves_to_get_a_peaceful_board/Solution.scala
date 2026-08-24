// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

object Solution {
  def minMoves(rooks: Array[Array[Int]]): Int = {
    var ans = 0
    java.util.Arrays.sort(rooks, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    var i = 0
    while (i < rooks.length) {
      ans += math.abs(rooks(i)(0) - i)
      i += 1
    }
    java.util.Arrays.sort(rooks, (a: Array[Int], b: Array[Int]) => Integer.compare(a(1), b(1)))
    var j = 0
    while (j < rooks.length) {
      ans += math.abs(rooks(j)(1) - j)
      j += 1
    }
    ans
  }
}
