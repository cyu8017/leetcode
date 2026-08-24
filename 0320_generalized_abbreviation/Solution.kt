// LeetCode 0320 - Generalized Abbreviation

// https://leetcode.com/problems/generalized-abbreviation/



class Solution {

    fun generateAbbreviations(word: String): List<String> {

        val result = mutableListOf<String>()

        backtrack(word, 0, "", 0, result)

        return result

    }



    private fun backtrack(

        word: String,

        index: Int,

        path: String,

        count: Int,

        result: MutableList<String>,

    ) {

        if (index == word.length) {

            result.add(path + if (count == 0) "" else count.toString())

            return

        }

        backtrack(word, index + 1, path, count + 1, result)

        val nextPath = path + (if (count == 0) "" else count.toString()) + word[index]

        backtrack(word, index + 1, nextPath, 0, result)

    }

}

