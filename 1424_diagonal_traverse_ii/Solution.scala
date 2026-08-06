import scala.collection.mutable
object Solution {
  def findDiagonalOrder(nums: List[List[Int]]): Array[Int] = {
    val diagonals = mutable.Map.empty[Int, mutable.ArrayBuffer[Int]]
    for ((row, r) <- nums.zipWithIndex; (value, c) <- row.zipWithIndex)
      diagonals.getOrElseUpdate(r + c, mutable.ArrayBuffer.empty) += value
    diagonals.toSeq.sortBy(_._1).flatMap(_._2.reverse).toArray
  }
}
