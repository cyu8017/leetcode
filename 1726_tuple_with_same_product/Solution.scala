// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

object Solution {
  def tupleSameProduct(nums: Array[Int]): Int = {
    val counts = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    for (i <- nums.indices; j <- i + 1 until nums.length) {
      counts(nums(i) * nums(j)) += 1
    }
    var result = 0L
    counts.values.foreach { count =>
      result += count.toLong * (count - 1) * 4
    }
    result.toInt
  }
}
