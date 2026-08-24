// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

class Solution {
    private fun gaps(fences: IntArray, bound: Int): MutableSet<Int> {
        val list = ArrayList<Int>()
        list.add(1)
        for (f in fences) list.add(f)
        list.add(bound)
        list.sort()
        val gaps = HashSet<Int>()
        for (i in list.indices) {
            for (j in i + 1 until list.size) {
                gaps.add(list[j] - list[i])
            }
        }
        return gaps
    }

    fun maximizeSquareArea(m: Int, n: Int, hFences: IntArray, vFences: IntArray): Int {
        val mod = 1_000_000_007
        val hg = gaps(hFences, m)
        val vg = gaps(vFences, n)
        var best = -1L
        for (g in hg) {
            if (vg.contains(g) && g > best) best = g.toLong()
        }
        if (best < 0) return -1
        return (best * best % mod).toInt()
    }
}
