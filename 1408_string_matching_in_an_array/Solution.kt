// LeetCode 1408 - String Matching in an Array
// https://leetcode.com/problems/string-matching-in-an-array/

class Solution {
    fun stringMatching(words: Array<String>): List<String> {
        val answer = ArrayList<String>()
        for (i in words.indices) {
            for (j in words.indices) {
                if (i != j && words[j].contains(words[i])) {
                    answer.add(words[i])
                    break
                }
            }
        }
        return answer
    }
}
