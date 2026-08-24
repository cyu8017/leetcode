// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

object Solution {
  def ipToCIDR(ip: String, n0: Int): List[String] = {
    def ipToInt(value: String): Long = {
      var result = 0L
      for (part <- value.split("\\.")) result = result * 256 + part.toLong
      result
    }
    def intToIp(value: Long): String =
      s"${(value >> 24) & 255}.${(value >> 16) & 255}.${(value >> 8) & 255}.${value & 255}"
    def bitLength(value0: Long): Int = {
      var value = value0
      var len = 0
      while (value > 0) {
        value >>= 1
        len += 1
      }
      len
    }
    var start = ipToInt(ip)
    var n = n0
    val answer = scala.collection.mutable.ArrayBuffer.empty[String]
    while (n > 0) {
      var lowbit = if (start == 0) 1L << 32 else start & -start
      while (lowbit > n) lowbit >>= 1
      val mask = 32 - (bitLength(lowbit) - 1)
      answer += intToIp(start) + "/" + mask
      start += lowbit
      n -= lowbit.toInt
    }
    answer.toList
  }
}
