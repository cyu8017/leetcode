// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/


class MapSum {
    private val map = HashMap<String, Int>()

    fun insert(key: String, `val`: Int) {
        map[key] = `val`
    }

    fun sum(prefix: String): Int {
        var total = 0
        for ((key, value) in map) {
            if (key.startsWith(prefix)) total += value
        }
        return total
    }
}
