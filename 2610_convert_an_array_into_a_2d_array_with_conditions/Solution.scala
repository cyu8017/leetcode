// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

object Solution {
  def findMatrix(nums: Array[Int]): List[List[Int]] = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    val ans = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Int]]
    nums.foreach { x =>
      val f = freq.getOrElse(x, 0)
      if (f == ans.size) ans += scala.collection.mutable.ArrayBuffer.empty[Int]
      ans(f) += x
      freq(x) = f + 1
    }
    ans.map(_.toList).toList
  }
}
