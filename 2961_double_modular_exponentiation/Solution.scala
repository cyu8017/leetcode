// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

object Solution {
  private def modPow(a0: Long, b0: Long, mod: Long): Long = {
    var res = 1L % mod
    var a = a0 % mod
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % mod
      a = a * a % mod
      b >>= 1
    }
    res
  }

  def getGoodIndices(variables: Array[Array[Int]], target: Int): List[Int] = {
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    var i = 0
    while (i < variables.length) {
      val v = variables(i)
      if (modPow(modPow(v(0).toLong, v(1).toLong, 10), v(2).toLong, v(3).toLong) == target) ans += i
      i += 1
    }
    ans.toList
  }
}
