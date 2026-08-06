// LeetCode 1534 - Count Good Triplets
// https://leetcode.com/problems/count-good-triplets/

object Solution {
  def countGoodTriplets(arr: Array[Int], a: Int, b: Int, c: Int): Int = {
    var ans = 0
    val n = arr.length
    for (i <- 0 until n; j <- i + 1 until n; k <- j + 1 until n) {
      if (math.abs(arr(i) - arr(j)) <= a && math.abs(arr(j) - arr(k)) <= b && math.abs(arr(i) - arr(k)) <= c)
        ans += 1
    }
    ans
  }
}
