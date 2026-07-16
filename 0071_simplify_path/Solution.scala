// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

object Solution {
  def simplifyPath(path: String): String = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[String]

    path.split("/").foreach { part =>
      if (part.nonEmpty && part != ".") {
        if (part == "..") {
          if (stack.nonEmpty) stack.remove(stack.length - 1)
        } else {
          stack += part
        }
      }
    }

    "/" + stack.mkString("/")
  }
}
