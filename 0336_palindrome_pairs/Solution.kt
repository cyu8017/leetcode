// LeetCode 0336 - Palindrome Pairs

// https://leetcode.com/problems/palindrome-pairs/



class Solution {

    fun palindromePairs(words: Array<String>): List<List<Int>> {

        val wordMap = words.withIndex().associate { it.value to it.index }

        val result = mutableSetOf<Pair<Int, Int>>()



        for ((index, word) in words.withIndex()) {

            for (split in 0..word.length) {

                val left = word.substring(0, split)

                val right = word.substring(split)

                if (left == left.reversed()) {

                    val reversedRight = right.reversed()

                    val otherIndex = wordMap[reversedRight]

                    if (otherIndex != null && otherIndex != index) {

                        result.add(otherIndex to index)

                    }

                }

                if (right == right.reversed()) {

                    val reversedLeft = left.reversed()

                    val otherIndex = wordMap[reversedLeft]

                    if (otherIndex != null && otherIndex != index) {

                        result.add(index to otherIndex)

                    }

                }

            }

        }



        return result.map { listOf(it.first, it.second) }

    }

}
