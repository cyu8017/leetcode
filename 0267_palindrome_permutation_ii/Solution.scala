// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

object Solution {
  def generatePalindromes(s: String): List[String] = {
    val counts = scala.collection.mutable.Map.empty[Char, Int]
    s.foreach { char =>
      counts(char) = counts.getOrElse(char, 0) + 1
    }

    val oddChars = counts.filter(_._2 % 2 != 0).keys.toList
    if (oddChars.size > 1) {
      return List.empty[String]
    }
    val middle = if (oddChars.nonEmpty) oddChars.head.toString else ""

    val half = counts.toList.sortBy(_._1).flatMap { case (char, count) =>
      List.fill(count / 2)(char)
    }.toArray

    val result = scala.collection.mutable.ListBuffer.empty[String]
    val used = Array.fill(half.length)(false)
    val path = Array.fill(half.length)(' ')

    def backtrack(depth: Int): Unit = {
      if (depth == half.length) {
        val prefix = path.mkString
        result += prefix + middle + prefix.reverse
        return
      }
      var index = 0
      while (index < half.length) {
        if (!used(index)) {
          if (!(index > 0 && half(index) == half(index - 1) && !used(index - 1))) {
            used(index) = true
            path(depth) = half(index)
            backtrack(depth + 1)
            used(index) = false
          }
        }
        index += 1
      }
    }

    backtrack(0)
    result.toList
  }
}
