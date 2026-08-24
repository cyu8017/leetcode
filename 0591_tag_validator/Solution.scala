// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

import scala.collection.mutable

object Solution {
  def isValid(code: String): Boolean = {
    val stack = mutable.ArrayBuffer.empty[String]
    var i = 0
    val n = code.length
    while (i < n) {
      if (code.startsWith("<![CDATA[", i)) {
        if (stack.isEmpty) return false
        val j = code.indexOf("]]>", i + 9)
        if (j < 0) return false
        i = j + 3
      } else if (code.startsWith("</", i)) {
        val j = code.indexOf('>', i + 2)
        if (j < 0) return false
        val tag = code.substring(i + 2, j)
        if (stack.isEmpty || stack.last != tag) return false
        stack.remove(stack.size - 1)
        i = j + 1
        if (stack.isEmpty && i < n) return false
      } else if (code.charAt(i) == '<') {
        val j = code.indexOf('>', i + 1)
        if (j < 0) return false
        val tag = code.substring(i + 1, j)
        if (tag.isEmpty || tag.length > 9) return false
        var k = 0
        while (k < tag.length) {
          val ch = tag.charAt(k)
          if (ch < 'A' || ch > 'Z') return false
          k += 1
        }
        stack += tag
        i = j + 1
      } else {
        if (stack.isEmpty) return false
        i += 1
      }
    }
    stack.isEmpty
  }
}
