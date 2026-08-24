// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

object Solution {
  def splitIntoFibonacci(num: String): List[Int] = {
    val path = scala.collection.mutable.ListBuffer.empty[Int]
    def dfs(start: Int): Boolean = {
      val n = num.length
      if (start == n) return path.length >= 3
      var value = 0L
      var end = start
      while (end < n) {
        if (num.charAt(start) == '0' && end > start) return false
        value = value * 10 + (num.charAt(end) - '0')
        if (value > Int.MaxValue) return false
        if (path.length >= 2) {
          val total = path(path.length - 1).toLong + path(path.length - 2)
          if (value < total) { end += 1; }
          else if (value > total) return false
          else {
            path += value.toInt
            if (dfs(end + 1)) return true
            path.remove(path.length - 1)
            end += 1
          }
        } else {
          path += value.toInt
          if (dfs(end + 1)) return true
          path.remove(path.length - 1)
          end += 1
        }
      }
      false
    }
    dfs(0)
    path.toList
  }
}
