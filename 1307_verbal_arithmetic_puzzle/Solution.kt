// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

class Solution {
    fun isSolvable(words: Array<String>, result: String): Boolean {
        if (words.maxOf { it.length } > result.length) return false
        val letters = (words.joinToString("") + result).toSet()
        if (letters.size > 10) return false
        val leading = mutableSetOf<Char>()
        for (word in words) if (word.length > 1) leading.add(word[0])
        if (result.length > 1) leading.add(result[0])
        val value = mutableMapOf<Char, Int>()
        val used = BooleanArray(10)
        val width = result.length

        fun solve(column: Int, row: Int, total: Int): Boolean {
            if (column == width) return total == 0
            if (row < words.size) {
                if (column >= words[row].length) return solve(column, row + 1, total)
                val ch = words[row][words[row].length - 1 - column]
                if (ch in value) return solve(column, row + 1, total + value[ch]!!)
                for (digit in 0..9) {
                    if (!used[digit] && (digit != 0 || ch !in leading)) {
                        value[ch] = digit
                        used[digit] = true
                        if (solve(column, row + 1, total + digit)) return true
                        used[digit] = false
                        value.remove(ch)
                    }
                }
                return false
            }
            val ch = result[result.length - 1 - column]
            val digit = total % 10
            val carry = total / 10
            if (ch in value) return value[ch] == digit && solve(column + 1, 0, carry)
            if (used[digit] || (digit == 0 && ch in leading)) return false
            value[ch] = digit
            used[digit] = true
            val ok = solve(column + 1, 0, carry)
            used[digit] = false
            value.remove(ch)
            return ok
        }

        return solve(0, 0, 0)
    }
}
