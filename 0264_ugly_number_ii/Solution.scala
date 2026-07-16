// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

object Solution {
  def nthUglyNumber(n: Int): Int = {
    val ugly = scala.collection.mutable.ArrayBuffer(1)
    var index2 = 0
    var index3 = 0
    var index5 = 0
    while (ugly.length < n) {
      val nextUgly = math.min(
        ugly(index2) * 2,
        math.min(ugly(index3) * 3, ugly(index5) * 5)
      )
      ugly += nextUgly
      if (nextUgly == ugly(index2) * 2) {
        index2 += 1
      }
      if (nextUgly == ugly(index3) * 3) {
        index3 += 1
      }
      if (nextUgly == ugly(index5) * 5) {
        index5 += 1
      }
    }
    ugly.last
  }
}
