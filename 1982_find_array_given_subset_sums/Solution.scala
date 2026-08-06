// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

object Solution {
  def recoverArray(n: Int, sums: Array[Int]): Array[Int] = {
    var cur = sums.sorted
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (_ <- 0 until n) {
      val d = cur(1) - cur(0)
      val count = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
      for (x <- cur) count(x) += 1
      val without = scala.collection.mutable.ArrayBuffer.empty[Int]
      val withD = scala.collection.mutable.ArrayBuffer.empty[Int]
      for (x <- cur if count(x) > 0) {
        count(x) -= 1
        count(x + d) -= 1
        without += x
        withD += x + d
      }
      if (without.contains(0)) {
        ans += d
        cur = without.toArray
      } else {
        ans += -d
        cur = withD.toArray
      }
    }
    ans.toArray
  }
}
