// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

object Solution {
  def getPermutation(n: Int, k: Int): String = {
    val numbers = scala.collection.mutable.ListBuffer.range(1, n + 1)
    val factorials = Array.fill(n)(1)

    var i = 1
    while (i < n) {
      factorials(i) = factorials(i - 1) * i
      i += 1
    }

    var remaining = k - 1
    val result = new StringBuilder

    var pos = n - 1
    while (pos >= 0) {
      val index = remaining / factorials(pos)
      result.append(numbers(index))
      numbers.remove(index)
      remaining %= factorials(pos)
      pos -= 1
    }

    result.toString()
  }
}
