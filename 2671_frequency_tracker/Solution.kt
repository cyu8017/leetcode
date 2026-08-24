// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker {
    private val freq = HashMap<Int, Int>()
    private val count = HashMap<Int, Int>()

    fun add(number: Int) {
        val old = freq.getOrDefault(number, 0)
        if (old > 0) count[old] = count.getOrDefault(old, 0) - 1
        freq[number] = old + 1
        count[old + 1] = count.getOrDefault(old + 1, 0) + 1
    }

    fun deleteOne(number: Int) {
        val old = freq.getOrDefault(number, 0)
        if (old == 0) return
        count[old] = count.getOrDefault(old, 0) - 1
        freq[number] = old - 1
        if (old - 1 > 0) count[old - 1] = count.getOrDefault(old - 1, 0) + 1
    }

    fun hasFrequency(frequency: Int): Boolean = count.getOrDefault(frequency, 0) > 0
}
