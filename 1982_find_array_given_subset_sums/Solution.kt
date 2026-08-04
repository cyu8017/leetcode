// LeetCode 1982
// https://leetcode.com/problems/find-array-given-subset-sums/

class Solution {
    fun recoverArray(n: Int, sums: IntArray): IntArray {
        var cur = sums.sorted().toMutableList()
        val ans = IntArray(n)
        for (t in 0 until n) {
            val d = cur[1] - cur[0]
            val count = HashMap<Int, Int>()
            for (x in cur) count[x] = count.getOrDefault(x, 0) + 1
            val without = mutableListOf<Int>()
            val withD = mutableListOf<Int>()
            for (x in cur) {
                if (count.getOrDefault(x, 0) == 0) continue
                count[x] = count[x]!! - 1
                count[x + d] = count.getOrDefault(x + d, 0) - 1
                without.add(x)
                withD.add(x + d)
            }
            if (0 in without) {
                ans[t] = d
                cur = without
            } else {
                ans[t] = -d
                cur = withD
            }
        }
        return ans
    }
}
