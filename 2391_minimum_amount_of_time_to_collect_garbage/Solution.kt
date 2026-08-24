// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution {
    fun garbageCollection(garbage: Array<String>, travel: IntArray): Int {
        var ans = 0
        var lastM = 0
        var lastP = 0
        var lastG = 0
        for (i in garbage.indices) {
            ans += garbage[i].length
            for (c in garbage[i]) {
                when (c) {
                    'M' -> lastM = i
                    'P' -> lastP = i
                    else -> lastG = i
                }
            }
        }
        val pref = IntArray(travel.size + 1)
        for (i in travel.indices) pref[i + 1] = pref[i] + travel[i]
        ans += pref[lastM] + pref[lastP] + pref[lastG]
        return ans
    }
}
