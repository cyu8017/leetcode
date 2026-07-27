// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution {
    fun alertNames(keyName: Array<String>, keyTime: Array<String>): List<String> {
        val times = HashMap<String, MutableList<Int>>()
        for (i in keyName.indices) {
            val parts = keyTime[i].split(":")
            val mins = parts[0].toInt() * 60 + parts[1].toInt()
            times.getOrPut(keyName[i]) { mutableListOf() }.add(mins)
        }
        val ans = mutableListOf<String>()
        for ((name, a) in times) {
            a.sort()
            var alert = false
            for (i in 0 until a.size - 2) {
                if (a[i + 2] - a[i] <= 60) {
                    alert = true
                    break
                }
            }
            if (alert) ans.add(name)
        }
        return ans.sorted()
    }
}
