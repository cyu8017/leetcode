// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution {
    private val mapping = arrayOf(
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    )

    fun letterCombinations(digits: String): List<String> {
        if (digits.isEmpty()) {
            return emptyList()
        }

        val result = mutableListOf<String>()
        val path = StringBuilder()

        fun backtrack(index: Int) {
            if (index == digits.length) {
                result.add(path.toString())
                return
            }
            for (ch in mapping[digits[index] - '0']) {
                path.append(ch)
                backtrack(index + 1)
                path.deleteCharAt(path.length - 1)
            }
        }

        backtrack(0)
        return result
    }
}
