// LeetCode 1348 - Tweet Counts Per Frequency
// https://leetcode.com/problems/tweet-counts-per-frequency/

class TweetCounts {
    private val times = HashMap<String, MutableList<Int>>()

    fun recordTweet(tweetName: String, time: Int) {
        val list = times.getOrPut(tweetName) { mutableListOf() }
        val idx = list.binarySearch(time).let { if (it < 0) -it - 1 else it }
        list.add(idx, time)
    }

    fun getTweetCountsPerFrequency(
        freq: String,
        tweetName: String,
        startTime: Int,
        endTime: Int
    ): List<Int> {
        val size = when (freq) {
            "minute" -> 60
            "hour" -> 3600
            else -> 86400
        }
        val list = times[tweetName] ?: emptyList()
        val answer = mutableListOf<Int>()
        var start = startTime
        while (start <= endTime) {
            val end = minOf(endTime, start + size - 1)
            answer.add(upperBound(list, end) - lowerBound(list, start))
            start += size
        }
        return answer
    }

    private fun lowerBound(list: List<Int>, target: Int): Int {
        var lo = 0
        var hi = list.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (list[mid] < target) lo = mid + 1 else hi = mid
        }
        return lo
    }

    private fun upperBound(list: List<Int>, target: Int): Int {
        var lo = 0
        var hi = list.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (list[mid] <= target) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
