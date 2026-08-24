// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

import scala.collection.mutable

object Solution {
  def findDuplicate(paths: Array[String]): List[List[String]] = {
    val contentToPaths = mutable.Map.empty[String, mutable.ArrayBuffer[String]]
    paths.foreach { entry =>
      val tokens = entry.split(" ")
      val directory = tokens(0)
      var i = 1
      while (i < tokens.length) {
        val fileInfo = tokens(i)
        val open = fileInfo.indexOf('(')
        val name = fileInfo.substring(0, open)
        val content = fileInfo.substring(open + 1, fileInfo.length - 1)
        contentToPaths.getOrElseUpdate(content, mutable.ArrayBuffer.empty[String]) += (directory + "/" + name)
        i += 1
      }
    }
    val result = mutable.ArrayBuffer.empty[List[String]]
    contentToPaths.values.foreach { group =>
      if (group.size > 1) result += group.toList
    }
    result.toList
  }
}
