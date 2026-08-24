// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/

object Solution {
  def getDataframeSize(players: Any): Array[Int] = {
    players match {
      case null => Array(0, 0)
      case rows: Array[_] if rows.isEmpty => Array(0, 0)
      case rows: Array[Array[Int]] => Array(rows.length, rows.headOption.map(_.length).getOrElse(0))
      case rows: Seq[_] if rows.isEmpty => Array(0, 0)
      case rows: Seq[_] =>
        val cols = rows.head match {
          case first: Seq[_] => first.length
          case first: Map[_, _] => first.size
          case first: Array[_] => first.length
          case _ => 0
        }
        Array(rows.length, cols)
      case _ => Array(0, 0)
    }
  }
}
