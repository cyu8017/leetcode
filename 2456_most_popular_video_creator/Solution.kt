// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

class Solution {
    private class Info(var total: Long, var bestID: String, var bestViews: Int)

    fun mostPopularCreator(creators: Array<String>, ids: Array<String>, views: IntArray): List<List<String>> {
        val mp = HashMap<String, Info>()
        var maxTotal = 0L
        for (i in creators.indices) {
            val info = mp[creators[i]]
            if (info == null) {
                mp[creators[i]] = Info(views[i].toLong(), ids[i], views[i])
            } else {
                info.total += views[i]
                if (views[i] > info.bestViews || (views[i] == info.bestViews && ids[i] < info.bestID)) {
                    info.bestViews = views[i]
                    info.bestID = ids[i]
                }
            }
            maxTotal = maxOf(maxTotal, mp[creators[i]]!!.total)
        }
        val ans = ArrayList<List<String>>()
        for ((key, value) in mp) {
            if (value.total == maxTotal) ans.add(listOf(key, value.bestID))
        }
        return ans
    }
}
