// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

object Solution {
  def restoreIpAddresses(s: String): List[String] = {
    val result = scala.collection.mutable.ListBuffer.empty[String]
    val path = scala.collection.mutable.ArrayBuffer.empty[String]

    def backtrack(start: Int): Unit = {
      if (path.length == 4) {
        if (start == s.length) {
          result += path.mkString(".")
        }
        return
      }

      for (length <- 1 to 3) {
        if (start + length <= s.length) {
          val part = s.substring(start, start + length)
          if (!(part.startsWith("0") && part.length > 1) && part.toInt <= 255) {
            path += part
            backtrack(start + length)
            path.remove(path.length - 1)
          }
        }
      }
    }

    backtrack(0)
    result.toList
  }
}
