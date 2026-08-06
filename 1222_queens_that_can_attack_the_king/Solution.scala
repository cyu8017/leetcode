// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

object Solution {
  def queensAttacktheKing(queens: Array[Array[Int]], king: Array[Int]): List[List[Int]] = {
    val occupied = queens.map(q => (q(0), q(1))).toSet
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    for (dr <- -1 to 1; dc <- -1 to 1 if !(dr == 0 && dc == 0)) {
      var r = king(0) + dr
      var c = king(1) + dc
      var found = false
      while (r >= 0 && r < 8 && c >= 0 && c < 8 && !found) {
        if (occupied.contains((r, c))) {
          answer += List(r, c)
          found = true
        } else {
          r += dr
          c += dc
        }
      }
    }
    answer.toList
  }
}
