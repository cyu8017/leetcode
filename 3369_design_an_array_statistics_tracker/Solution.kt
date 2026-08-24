// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker {
    private val arr = ArrayList<Int>()
    private var sum = 0L
    private val freq = HashMap<Int, Int>()
    private var modeFreq = 0
    private val modes = HashSet<Int>()

    fun addNumber(num: Int) {
        arr.add(num)
        sum += num
        val f = (freq[num] ?: 0) + 1
        freq[num] = f
        if (f > modeFreq) {
            modeFreq = f
            modes.clear()
            modes.add(num)
        } else if (f == modeFreq) {
            modes.add(num)
        }
    }

    fun removeFirst() {
        if (arr.isEmpty()) return
        val num = arr.removeAt(0)
        sum -= num
        val f = freq[num]!! - 1
        if (f == 0) freq.remove(num) else freq[num] = f
        modeFreq = 0
        modes.clear()
        for ((v, ff) in freq) {
            if (ff > modeFreq) {
                modeFreq = ff
                modes.clear()
                modes.add(v)
            } else if (ff == modeFreq) {
                modes.add(v)
            }
        }
    }

    fun getMean(): Int {
        if (arr.isEmpty()) return 0
        return (sum / arr.size).toInt()
    }

    fun getMedian(): Int {
        val n = arr.size
        val tmp = ArrayList(arr)
        tmp.sort()
        return if (n % 2 == 1) tmp[n / 2] else tmp[n / 2 - 1]
    }

    fun getMode(): Int {
        var best = Long.MAX_VALUE
        for (v in modes) if (v < best) best = v.toLong()
        if (best == Long.MAX_VALUE) return 0
        return best.toInt()
    }
}
