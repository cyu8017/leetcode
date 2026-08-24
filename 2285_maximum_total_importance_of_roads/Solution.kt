// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution {

    fun maximumImportance(n: Int, roads: Array<IntArray>): Long {

            var deg = IntArray(n)
            for (r in roads) { deg[r[0]]++; deg[r[1]]++; }
            deg.sort()
            var ans = 0
            for (i in 0 until n) { ans += deg[i] * (i + 1) }
            return ans

    }

}
