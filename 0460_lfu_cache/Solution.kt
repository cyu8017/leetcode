// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

class LFUCache(private val capacity: Int) {
    private var minFreq = 0
    private val keyValues = HashMap<Int, Int>()
    private val keyFreqs = HashMap<Int, Int>()
    private val freqKeys = HashMap<Int, MutableList<Int>>()

    private fun touch(key: Int) {
        val freq = keyFreqs.getValue(key)
        val bucket = freqKeys.getValue(freq)
        bucket.remove(key)
        if (bucket.isEmpty() && freq == minFreq) {
            minFreq++
        }
        val nextFreq = freq + 1
        keyFreqs[key] = nextFreq
        freqKeys.getOrPut(nextFreq) { mutableListOf() }.add(key)
    }

    fun get(key: Int): Int {
        if (key !in keyValues) {
            return -1
        }
        touch(key)
        return keyValues.getValue(key)
    }

    fun put(key: Int, value: Int) {
        if (capacity == 0) {
            return
        }
        if (key in keyValues) {
            keyValues[key] = value
            touch(key)
            return
        }
        if (keyValues.size >= capacity) {
            val evict = freqKeys.getValue(minFreq).removeAt(0)
            keyValues.remove(evict)
            keyFreqs.remove(evict)
        }
        keyValues[key] = value
        keyFreqs[key] = 1
        freqKeys.getOrPut(1) { mutableListOf() }.add(key)
        minFreq = 1
    }
}
