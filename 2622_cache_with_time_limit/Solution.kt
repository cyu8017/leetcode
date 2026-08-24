// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache {
    private class Entry(var value: Int, var expire: Long)

    private val data = HashMap<Int, Entry>()
    private val start = System.nanoTime()

    private fun nowMs(): Long = (System.nanoTime() - start) / 1_000_000L

    fun set(key: Int, value: Int, duration: Int): Boolean {
        val now = nowMs()
        val e = data[key]
        val alive = e != null && e.expire > now
        data[key] = Entry(value, now + duration)
        return alive
    }

    fun get(key: Int): Int {
        val now = nowMs()
        val e = data[key]
        if (e == null || e.expire <= now) return -1
        return e.value
    }

    fun count(): Int {
        val now = nowMs()
        var cnt = 0
        val dead = ArrayList<Int>()
        for ((k, v) in data) {
            if (v.expire > now) cnt++ else dead.add(k)
        }
        for (k in dead) data.remove(k)
        return cnt
    }
}
