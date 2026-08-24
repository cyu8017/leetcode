// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

object Solution {
  def productQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val mod = 1000000007
    val powers = scala.collection.mutable.ArrayBuffer.empty[Int]
    var bit = 0
    while (bit < 31) {
      if (((n >> bit) & 1) != 0) powers += (1 << bit)
      bit += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      var prod = 1L
      var j = queries(i)(0)
      while (j <= queries(i)(1)) {
        prod = prod * powers(j) % mod
        j += 1
      }
      ans(i) = prod.toInt
      i += 1
    }
    ans
  }
}
