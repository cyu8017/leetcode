// LeetCode 0408 - Valid Word Abbreviation

// https://leetcode.com/problems/valid-word-abbreviation/



object Solution {

  def validWordAbbreviation(word: String, abbr: String): Boolean = {

    var i = 0

    var j = 0



    while (i < word.length && j < abbr.length) {

      if (abbr(j).isDigit) {

        if (abbr(j) == '0') {

          return false

        }



        var number = 0



        while (j < abbr.length && abbr(j).isDigit) {

          number = number * 10 + abbr(j).asDigit

          j += 1

        }



        i += number

      } else {

        if (word(i) != abbr(j)) {

          return false

        }



        i += 1

        j += 1

      }

    }



    i == word.length && j == abbr.length

  }

}
