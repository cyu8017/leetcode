// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

object Solution {
  def maxNumberOfApples(weight: Array[Int]): Int = {
    val sorted = weight.sorted
    var total = 0
    for (i <- sorted.indices) {
      total += sorted(i)
      if (total > 5000) return i
    }
    sorted.length
  }
}
