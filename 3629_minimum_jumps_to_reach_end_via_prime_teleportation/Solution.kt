// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

class Solution {
    companion object {
        private const val MX = 1000001
        private var factorsCache: Array<ArrayList<Int>>? = null

        private fun factors(): Array<ArrayList<Int>> {
            if (factorsCache == null) {
                val f = Array(MX) { ArrayList<Int>() }
                for (i in 2 until MX) {
                    if (f[i].isEmpty()) {
                        var j = i
                        while (j < MX) {
                            f[j].add(i)
                            j += i
                        }
                    }
                }
                factorsCache = f
            }
            return factorsCache!!
        }
    }

    fun minJumps(nums: IntArray): Int {
        val fac = factors()
        val n = nums.size
        val g = HashMap<Int, ArrayList<Int>>()
        for (i in 0 until n) {
            for (p in fac[nums[i]]) {
                g.getOrPut(p) { ArrayList() }.add(i)
            }
        }
        var ans = 0
        val vis = BooleanArray(n)
        vis[0] = true
        var q = ArrayList<Int>()
        q.add(0)
        while (true) {
            val nq = ArrayList<Int>()
            for (i in q) {
                if (i == n - 1) return ans
                val idx = ArrayList(g.getOrDefault(nums[i], emptyList()))
                idx.add(i + 1)
                if (i > 0) idx.add(i - 1)
                for (j in idx) {
                    if (j in 0 until n && !vis[j]) {
                        vis[j] = true
                        nq.add(j)
                    }
                }
                g[nums[i]] = ArrayList()
            }
            q = nq
            ans++
        }
    }
}
