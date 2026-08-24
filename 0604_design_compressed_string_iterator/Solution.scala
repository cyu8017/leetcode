// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

import scala.collection.mutable

class StringIterator(compressedString: String) {
  private val chars = mutable.ArrayBuffer.empty[Char]
  private val counts = mutable.ArrayBuffer.empty[Int]
  private var index = 0

  {
    val n = compressedString.length
    var i = 0
    while (i < n) {
      val ch = compressedString.charAt(i)
      i += 1
      var j = i
      while (j < n && compressedString.charAt(j) >= '0' && compressedString.charAt(j) <= '9') j += 1
      chars += ch
      counts += compressedString.substring(i, j).toInt
      i = j
    }
  }

  def next(): Char = {
    if (!hasNext()) return ' '
    val ch = chars(index)
    counts(index) -= 1
    if (counts(index) == 0) index += 1
    ch
  }

  def hasNext(): Boolean = index < chars.size
}
