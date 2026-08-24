// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

class Solution {
    fun prisonAfterNDays(cells: IntArray, n: Int): IntArray {
        var n = n
        val seen = HashMap<String, Int>()
        var state = cells.copyOf()
        while (n > 0) {
            val key = state.contentToString()
            if (seen.containsKey(key)) {
                val cycle = seen[key]!! - n
                n %= cycle
                if (n == 0) break
            }
            seen[key] = n
            val nxt = IntArray(8)
            for (i in 1..6) nxt[i] = if (state[i - 1] == state[i + 1]) 1 else 0
            state = nxt
            n--
        }
        return state
    }
}
