// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

object Solution {
  def maxLength(arr: List[String]): Int = {
    var masks = List((0, 0))
    for (word <- arr) {
      var mask = 0
      var ok = true
      for (ch <- word) {
        val bit = 1 << (ch - 'a')
        if ((mask & bit) != 0) ok = false
        mask |= bit
      }
      if (ok && Integer.bitCount(mask) == word.length) {
        masks = masks ++ masks.collect { case (used, length) if (used & mask) == 0 => (used | mask, length + word.length) }
      }
    }
    masks.map(_._2).max
  }
}
