// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

class FirstUnique(nums: IntArray) {
    private val counts = mutableMapOf<Int, Int>()
    private val unique = LinkedHashMap<Int, Boolean>()

    init {
        for (value in nums) add(value)
    }

    fun showFirstUnique(): Int = unique.keys.firstOrNull() ?: -1

    fun add(value: Int) {
        counts[value] = counts.getOrDefault(value, 0) + 1
        if (counts[value] == 1) {
            unique[value] = true
        } else {
            unique.remove(value)
        }
    }
}
