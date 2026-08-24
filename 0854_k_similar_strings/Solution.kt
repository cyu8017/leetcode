// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

class Solution {
    private var s2: String? = null

    fun kSimilarity(s1: String, s2: String): Int {
        var s2 = s2
        if ((s1 == s2)) return 0
        this.s2 = s2
        var queue = ArrayDeque<String>()
        var dist = HashMap<String, Int>()
        queue.offer(s1)
        dist[s1] = 0
        while (!queue.isEmpty()) {
            var cur = queue.poll()
            var d = dist[cur]
            for (nxt in neighbors(cur)) {
                if ((nxt == s2)) return d + 1
                if (!dist.containsKey(nxt)) {
                    dist[nxt] = d + 1
                    queue.offer(nxt)
                }
            }
        }
        return -1
    }

    private fun neighbors(s: String): MutableList<String> {
        var arr = s.toCharArray()
        var i = 0
        while (arr[i] == s2[i]) i++
        var res = ArrayList<String>()
        for (j in i + 1 until arr.size) {
            if (arr[j] == s2[i] && arr[j] != s2[j]) {
                var tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                res.add(String(arr))
                arr[j] = arr[i]
                arr[i] = tmp
            }
        }
        return res
    }
}
