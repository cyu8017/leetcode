// LeetCode 0411 - Minimum Unique Word Abbreviation

// https://leetcode.com/problems/minimum-unique-word-abbreviation/



class Solution {

    private lateinit var target: String

    private lateinit var words: List<String>

    private var bestLen = 0

    private lateinit var result: String



    fun minAbbreviation(target: String, dictionary: List<String>): String {

        this.target = target

        this.words = dictionary.filter { it.length == target.length }

        bestLen = target.length + 1

        result = target

        dfs(0, mutableListOf(), 0)

        return result

    }



    private fun matches(word: String, abbr: String): Boolean {

        var index = 0

        var pointer = 0



        while (index < word.length && pointer < abbr.length) {

            if (abbr[pointer].isDigit()) {

                if (abbr[pointer] == '0') {

                    return false

                }



                var number = 0



                while (pointer < abbr.length && abbr[pointer].isDigit()) {

                    number = number * 10 + abbr[pointer].digitToInt()

                    pointer++

                }



                index += number

            } else {

                if (word[index] != abbr[pointer]) {

                    return false

                }



                index++

                pointer++

            }

        }



        return index == word.length && pointer == abbr.length

    }



    private fun valid(abbr: String): Boolean {

        if (!matches(target, abbr)) {

            return false

        }



        return words.all { !matches(it, abbr) }

    }



    private fun dfs(index: Int, parts: MutableList<String>, skip: Int) {

        if (index == target.length) {

            val abbr = parts.joinToString("") + if (skip != 0) skip.toString() else ""



            if (valid(abbr)) {

                if (abbr.length < bestLen || (abbr.length == bestLen && abbr < result)) {

                    bestLen = abbr.length

                    result = abbr

                }

            }



            return

        }



        dfs(index + 1, parts, skip + 1)



        val newParts = parts.toMutableList()



        if (skip != 0) {

            newParts.add(skip.toString())

        }



        newParts.add(target[index].toString())

        dfs(index + 1, newParts, 0)

    }

}
