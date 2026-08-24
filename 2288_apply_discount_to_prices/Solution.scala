// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

object Solution {
  def discountPrices(sentence: String, discount: Int): String = {
    val parts = sentence.split(" ")
    var i = 0
    while (i < parts.length) {
      val part = parts(i)
      if (part.length >= 2 && part.charAt(0) == '$') {
        var ok = true
        var j = 1
        while (j < part.length) {
          val ch = part.charAt(j)
          if (ch < '0' || ch > '9') ok = false
          j += 1
        }
        if (ok) {
          val value = part.substring(1).toLong
          val price = value * (100.0 - discount) / 100.0
          parts(i) = String.format("$%.2f", price)
        }
      }
      i += 1
    }
    parts.mkString(" ")
  }
}
