// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

object Solution {
  def smallestGoodBase(n: String): String = {
    val num = BigInt(n)
    var length = (math.log(num.toDouble) / math.log(2)).toInt + 1
    while (length > 1) {
      var low = BigInt(2)
      var high = num - 1
      while (low <= high) {
        val mid = low + (high - low) / 2
        var total = BigInt(1)
        var power = BigInt(1)
        var ok = true
        var i = 1
        while (i < length && ok) {
          power *= mid
          total += power
          if (total > num) ok = false
          i += 1
        }
        if (ok && total == num) return mid.toString
        if (!ok || total > num) high = mid - 1 else low = mid + 1
      }
      length -= 1
    }
    (num - 1).toString
  }
}
