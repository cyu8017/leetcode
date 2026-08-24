// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack {
    private val freq = HashMap<Int, Int>()
    private val group = HashMap<Int, MutableList<Int>>()
    private var maxfreq = 0

    fun push(`val`: Int) {
        val f = freq.getOrDefault(`val`, 0) + 1
        freq[`val`] = f
        maxfreq = maxOf(maxfreq, f)
        group.getOrPut(f) { mutableListOf() }.add(`val`)
    }

    fun pop(): Int {
        val list = group[maxfreq]!!
        val `val` = list.removeAt(list.size - 1)
        freq[`val`] = freq[`val`]!! - 1
        if (list.isEmpty()) maxfreq--
        return `val`
    }
}
