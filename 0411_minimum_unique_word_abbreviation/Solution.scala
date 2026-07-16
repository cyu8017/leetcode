// LeetCode 0411 - Minimum Unique Word Abbreviation

// https://leetcode.com/problems/minimum-unique-word-abbreviation/



object Solution {

  private var target = ""

  private var words = List.empty[String]

  private var bestLen = 0

  private var result = ""



  def minAbbreviation(target: String, dictionary: List[String]): String = {

    this.target = target

    this.words = dictionary.filter(_.length == target.length)

    bestLen = target.length + 1

    result = target

    dfs(0, List.empty, 0)

    result

  }



  private def matches(word: String, abbr: String): Boolean = {

    var index = 0

    var pointer = 0



    while (index < word.length && pointer < abbr.length) {

      if (abbr(pointer).isDigit) {

        if (abbr(pointer) == '0') {

          return false

        }



        var number = 0



        while (pointer < abbr.length && abbr(pointer).isDigit) {

          number = number * 10 + abbr(pointer).asDigit

          pointer += 1

        }



        index += number

      } else {

        if (word(index) != abbr(pointer)) {

          return false

        }



        index += 1

        pointer += 1

      }

    }



    index == word.length && pointer == abbr.length

  }



  private def valid(abbr: String): Boolean = {

    matches(target, abbr) && words.forall(word => !matches(word, abbr))

  }



  private def dfs(index: Int, parts: List[String], skip: Int): Unit = {

    if (index == target.length) {

      val abbr = parts.mkString + (if (skip != 0) skip.toString else "")



      if (valid(abbr)) {

        if (abbr.length < bestLen || (abbr.length == bestLen && abbr < result)) {

          bestLen = abbr.length

          result = abbr

        }

      }



      return

    }



    dfs(index + 1, parts, skip + 1)



    val newParts =

      if (skip != 0) parts :+ skip.toString :+ target(index).toString

      else parts :+ target(index).toString



    dfs(index + 1, newParts, 0)

  }

}
