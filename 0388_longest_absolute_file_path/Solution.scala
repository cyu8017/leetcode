// LeetCode 0388 - Longest Absolute File Path

// https://leetcode.com/problems/longest-absolute-file-path/



import scala.collection.mutable



object Solution {

  def lengthLongestPath(input: String): Int = {

    val stack = mutable.Stack.empty[Int]

    var maxLength = 0



    for (line <- input.split("\n")) {

      val depth = line.takeWhile(_ == '\t').length

      val name = line.substring(depth)



      while (stack.size > depth) {

        stack.pop()

      }



      if (name.contains('.')) {

        val prefix = if (stack.isEmpty) 0 else stack.top

        maxLength = math.max(maxLength, prefix + name.length)

      } else {

        val prefix = if (stack.isEmpty) 0 else stack.top

        stack.push(prefix + name.length + 1)

      }

    }



    maxLength

  }

}
