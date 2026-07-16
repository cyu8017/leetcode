// LeetCode 0408 - Valid Word Abbreviation

// https://leetcode.com/problems/valid-word-abbreviation/



class Solution {

    fun validWordAbbreviation(word: String, abbr: String): Boolean {

        var i = 0

        var j = 0



        while (i < word.length && j < abbr.length) {

            if (abbr[j].isDigit()) {

                if (abbr[j] == '0') {

                    return false

                }



                var number = 0



                while (j < abbr.length && abbr[j].isDigit()) {

                    number = number * 10 + abbr[j].digitToInt()

                    j++

                }



                i += number

            } else {

                if (word[i] != abbr[j]) {

                    return false

                }



                i++

                j++

            }

        }



        return i == word.length && j == abbr.length

    }

}
