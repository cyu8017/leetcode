// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

object Solution {
  private val ones = Array(
    "",
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
    "Seventeen", "Eighteen", "Nineteen"
  )
  private val tens = Array(
    "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
  )
  private val thousands = Array("", "Thousand", "Million", "Billion")

  def numberToWords(num: Int): String = {
    if (num == 0) return "Zero"

    val parts = scala.collection.mutable.ListBuffer.empty[String]
    var value = num
    var chunkIndex = 0
    while (value > 0) {
      val chunk = value % 1000
      if (chunk != 0) {
        var chunkWords = convertChunk(chunk)
        if (thousands(chunkIndex).nonEmpty) {
          chunkWords += s" ${thousands(chunkIndex)}"
        }
        parts += chunkWords
      }
      value /= 1000
      chunkIndex += 1
    }
    parts.reverse.mkString(" ")
  }

  private def convertChunk(value: Int): String = {
    if (value == 0) ""
    else if (value < 20) ones(value)
    else if (value < 100) {
      val tensPart = tens(value / 10)
      val onesPart = ones(value % 10)
      if (onesPart.isEmpty) tensPart else s"$tensPart $onesPart"
    } else {
      val hundreds = ones(value / 100)
      val remainder = convertChunk(value % 100)
      if (remainder.isEmpty) s"$hundreds Hundred" else s"$hundreds Hundred $remainder"
    }
  }
}
