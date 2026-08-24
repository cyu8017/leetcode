// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

object Solution {
  def kthCharacter(k: Long, operations: Array[Int]): Char = {
    var kk = k
    var shift = 0
    val ops = scala.collection.mutable.ArrayBuffer(operations: _*)
    while (ops.nonEmpty) {
      val op = ops.remove(ops.length - 1)
      val half = 1L << ops.length
      if (kk > half) {
        kk -= half
        if (op == 1) shift += 1
      }
    }
    ('a' + shift % 26).toChar
  }
}
