// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

object Solution {
  def maxPrice(items: Array[Array[Int]], capacity: Int): Double = {
    val sorted = items.sortBy(it => -it(0).toDouble / it(1))
    var ans = 0.0
    var remain = capacity
    sorted.foreach { it =>
      val price = it(0)
      val weight = it(1)
      if (remain >= weight) {
        ans += price
        remain -= weight
      } else {
        ans += price.toDouble * remain / weight
        remain = 0
        return if (remain > 0) -1 else ans
      }
    }
    if (remain > 0) -1 else ans
  }
}
