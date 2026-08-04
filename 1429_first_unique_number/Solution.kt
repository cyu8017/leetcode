// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

class FirstUnique(nums: IntArray) {
    private val freq = HashMap<Int, Int>()
    private val queue = ArrayDeque<Int>()

    init {
        for (x in nums) add(x)
    }

    fun showFirstUnique(): Int {
        while (queue.isNotEmpty() && freq[queue.first()]!! > 1) {
            queue.removeFirst()
        }
        return if (queue.isEmpty()) -1 else queue.first()
    }

    fun add(value: Int) {
        freq[value] = freq.getOrDefault(value, 0) + 1
        if (freq[value] == 1) queue.addLast(value)
    }
}
