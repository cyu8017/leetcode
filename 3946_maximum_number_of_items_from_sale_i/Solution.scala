// LeetCode 3946 - Maximum Number of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

object Solution {
  def maximumSaleItems(items: Array[Array[Int]], budget: Int): Int = {
    val f = new Array[Int](budget + 1)
    var mn = Int.MaxValue
    for (item <- items) {
      val factor = item(0)
      val price = item(1)
      mn = math.min(mn, price)
      var cnt = 0
      for (jItem <- items) {
        if (jItem(0) % factor == 0) cnt += 1
      }
      var j = budget
      while (j >= price) {
        f(j) = math.max(f(j), f(j - price) + cnt)
        j -= 1
      }
    }
    var ans = 0
    var i = 0
    while (i <= budget) {
      val extra = (budget - i) / mn
      ans = math.max(ans, f(i) + extra)
      i += 1
    }
    ans
  }
}
