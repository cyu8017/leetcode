// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

object Solution {
  def removeComments(source: Array[String]): List[String] = {
    val result = scala.collection.mutable.ArrayBuffer.empty[String]
    val buffer = new StringBuilder
    var inBlock = false
    for (line <- source) {
      var i = 0
      while (i < line.length) {
        if (inBlock) {
          if (i + 1 < line.length && line.charAt(i) == '*' && line.charAt(i + 1) == '/') {
            inBlock = false
            i += 2
          } else i += 1
        } else if (i + 1 < line.length && line.charAt(i) == '/' && line.charAt(i + 1) == '*') {
          inBlock = true
          i += 2
        } else if (i + 1 < line.length && line.charAt(i) == '/' && line.charAt(i + 1) == '/') {
          i = line.length
        } else {
          buffer.append(line.charAt(i))
          i += 1
        }
      }
      if (!inBlock && buffer.length > 0) {
        result += buffer.toString
        buffer.setLength(0)
      }
    }
    result.toList
  }
}
