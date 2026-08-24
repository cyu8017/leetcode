// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream {
    private var value: Int = 0
    private var k: Int = 0
    private var streak: Int = 0

    constructor(value: Int, k: Int) {
        this.value = value
        this.k = k
        streak = 0
    }

    fun consec(num: Int): Boolean {
        if (num == value) { streak = streak + 1 }
        else streak = 0
        return streak >= k
    }
}
