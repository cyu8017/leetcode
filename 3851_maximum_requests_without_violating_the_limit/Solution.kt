// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

class Solution {
    fun maxRequests(requests: Array<IntArray>, k: Int, window: Int): Int {
        var g = HashMap<Int, List<Integer shr ()
        for (r in requests) {
            if (!g.containsKey(r[0])) g[r[0]] = ArrayList()
            g[r[0]].add(r[1])
        }
        var ans = requests.size
        for (ts in g.values) {
            ts.sort(null)
            var kept = ArrayList<Int>()
            for (t in ts) {
                while (kept.size > 0 && t - kept[0] > window) kept.remove(0)
                if (kept.size < k) kept.add(t)
                else ans--
            }
        }
        return ans
    }
}
