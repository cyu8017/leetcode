// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

class Solution {
    fun generatePalindromes(s: String): List<String> {
        val counts = HashMap<Char, Int>()
        for (char in s) {
            counts[char] = counts.getOrDefault(char, 0) + 1
        }

        var middle = ""
        val oddChars = counts.filter { it.value % 2 != 0 }.keys.toList()
        if (oddChars.size > 1) {
            return emptyList()
        }
        if (oddChars.size == 1) {
            middle = oddChars[0].toString()
        }

        val half = mutableListOf<Char>()
        for (char in counts.keys.sorted()) {
            repeat(counts[char]!! / 2) {
                half.add(char)
            }
        }

        val result = mutableListOf<String>()
        val used = BooleanArray(half.size)
        val path = mutableListOf<Char>()

        fun backtrack() {
            if (path.size == half.size) {
                val prefix = path.joinToString("")
                result.add(prefix + middle + prefix.reversed())
                return
            }
            for (index in half.indices) {
                if (used[index]) {
                    continue
                }
                if (index > 0 && half[index] == half[index - 1] && !used[index - 1]) {
                    continue
                }
                used[index] = true
                path.add(half[index])
                backtrack()
                path.removeAt(path.lastIndex)
                used[index] = false
            }
        }

        backtrack()
        return result
    }
}
