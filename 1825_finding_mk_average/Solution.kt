// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

class MKAverage(private val m: Int, private val k: Int) {
    private val stream = ArrayDeque<Int>()

    fun addElement(num: Int) {
        stream.addLast(num)
    }

    fun calculateMKAverage(): Int {
        if (stream.size < m) return -1
        val window = stream.takeLast(m).sorted()
        val middle = window.subList(k, window.size - k)
        return middle.sum() / middle.size
    }
}
