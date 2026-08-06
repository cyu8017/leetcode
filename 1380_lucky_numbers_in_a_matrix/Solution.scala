object Solution {
  def luckyNumbers(matrix: Array[Array[Int]): List[Int] = {
    val minimums = matrix.map(_.min).toSet
    val maximums = matrix.head.indices.map(c => matrix.map(_(c)).max).toSet
    minimums.intersect(maximums).toList
  }
}
