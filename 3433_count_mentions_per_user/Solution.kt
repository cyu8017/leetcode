// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

class Solution {
    fun countMentions(numberOfUsers: Int, events: List<List<String>>): IntArray {
        val ev = events.sortedWith { a, b ->
            val ti = a[1].toInt()
            val tj = b[1].toInt()
            if (ti != tj) ti.compareTo(tj) else b[0].compareTo(a[0])
        }
        val online = BooleanArray(numberOfUsers) { true }
        val offlineUntil = IntArray(numberOfUsers)
        val ans = IntArray(numberOfUsers)
        for (e in ev) {
            val t = e[1].toInt()
            for (i in 0 until numberOfUsers) {
                if (!online[i] && offlineUntil[i] <= t) online[i] = true
            }
            if (e[0] == "OFFLINE") {
                val id = e[2].toInt()
                online[id] = false
                offlineUntil[id] = t + 60
            } else {
                when (val msg = e[2]) {
                    "ALL" -> for (i in 0 until numberOfUsers) ans[i]++
                    "HERE" -> for (i in 0 until numberOfUsers) if (online[i]) ans[i]++
                    else -> {
                        for (part in msg.split(" ")) {
                            ans[part.substring(2).toInt()]++
                        }
                    }
                }
            }
        }
        return ans
    }
}
