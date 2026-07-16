// LeetCode 0320 - Generalized Abbreviation

// https://leetcode.com/problems/generalized-abbreviation/



import scala.collection.mutable



object Solution {

  def generateAbbreviations(word: String): List[String] = {

    val result = mutable.ListBuffer.empty[String]

    backtrack(word, 0, "", 0, result)

    result.toList

  }



  private def backtrack(

      word: String,

      index: Int,

      path: String,

      count: Int,

      result: mutable.ListBuffer[String],

  ): Unit = {

    if (index == word.length) {

      result += path + (if (count == 0) "" else count.toString)

      return

    }

    backtrack(word, index + 1, path, count + 1, result)

    val nextPath = path + (if (count == 0) "" else count.toString) + word(index)

    backtrack(word, index + 1, nextPath, 0, result)

  }

}

