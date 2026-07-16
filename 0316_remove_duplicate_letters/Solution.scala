// LeetCode 0316 - Remove Duplicate Letters

// https://leetcode.com/problems/remove-duplicate-letters/



import scala.collection.mutable



object Solution {

  def removeDuplicateLetters(s: String): String = {

    val lastIndex = new Array[Int](26)

    for (index <- s.indices) {

      lastIndex(s(index) - 'a') = index

    }



    val stack = mutable.ListBuffer.empty[Char]

    val seen = mutable.Set.empty[Char]

    for (index <- s.indices) {

      val ch = s(index)

      if (seen.contains(ch)) {

        // skip duplicate

      } else {

        while (stack.nonEmpty && stack.last > ch && lastIndex(stack.last - 'a') > index) {

          seen.remove(stack.remove(stack.length - 1))

        }

        stack += ch

        seen.add(ch)

      }

    }

    stack.mkString

  }

}

