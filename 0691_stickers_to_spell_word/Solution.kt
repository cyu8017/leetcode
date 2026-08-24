// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

class Solution {
    private val chars = ArrayList<Char>()
    private val sticks = ArrayList<IntArray>()
    private val memo = HashMap<String, Int>()

    private fun key(state: IntArray): String = state.joinToString(",")

    private fun dfs(state: IntArray): Int {
        val k = key(state)
        memo[k]?.let { return it }
        var i = 0
        while (i < state.size && state[i] == 0) i++
        if (i == state.size) {
            memo[k] = 0
            return 0
        }
        val first = chars[i]
        var best = Int.MAX_VALUE / 4
        for (stick in sticks) {
            if (stick[first - 'a'] == 0) continue
            val nxt = state.copyOf()
            for (j in chars.indices) {
                nxt[j] = maxOf(0, nxt[j] - stick[chars[j] - 'a'])
            }
            best = minOf(best, 1 + dfs(nxt))
        }
        memo[k] = best
        return best
    }

    fun minStickers(stickers: Array<String>, target: String): Int {
        val need = IntArray(26)
        for (ch in target) need[ch - 'a']++
        chars.clear()
        for (i in 0 until 26) if (need[i] > 0) chars.add(('a'.code + i).toChar())
        sticks.clear()
        for (sticker in stickers) {
            val counts = IntArray(26)
            for (ch in sticker) counts[ch - 'a']++
            var useful = false
            for (ch in chars) if (counts[ch - 'a'] > 0) { useful = true; break }
            if (useful) sticks.add(counts)
        }
        memo.clear()
        val state = IntArray(chars.size)
        for (i in chars.indices) state[i] = need[chars[i] - 'a']
        val result = dfs(state)
        return if (result >= Int.MAX_VALUE / 4) -1 else result
    }
}
