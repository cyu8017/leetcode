// LeetCode 0346 - Moving Average from Data Stream

// https://leetcode.com/problems/moving-average-from-data-stream/



class MovingAverage(private val size: Int) {

    private val values = ArrayDeque<Int>()

    private var total = 0



    fun next(`val`: Int): Double {

        values.addLast(`val`)

        total += `val`

        if (values.size > size) {

            total -= values.removeFirst()

        }

        return total.toDouble() / values.size

    }

}
