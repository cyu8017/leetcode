// LeetCode 3799 - Word Squares Ii
// https://leetcode.com/problems/word-squares-ii/

class Solution {
    fun wordSquares(words: Array<String>): MutableList<MutableList<String>> {
        words.sort()
        val n = words.size
        val ans = ArrayList<MutableList<String>>()
        for (i in 0 until n) {
            val top = words[i]
            for (j in 0 until n) {
                if (j == i) continue
                val left = words[j]
                for (k in 0 until n) {
                    if (k == j || k == i) continue
                    val right = words[k]
                    for (h in 0 until n) {
                        if (h == k || h == j || h == i) continue
                        val bottom = words[h]
                        if (top[0] == left[0] && top[3] == right[0] &&
                            bottom[0] == left[3] && bottom[3] == right[3]
                        ) {
                            ans.add(arrayListOf(top, left, right, bottom))
                        }
                    }
                }
            }
        }
        return ans
    }
}
