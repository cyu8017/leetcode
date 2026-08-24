// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

class Solution {
    fun countCoveredBuildings(n: Int, buildings: Array<IntArray>): Int {
        var g1 = HashMap<Int, MutableList<Int>>()
        var g2 = HashMap<Int, MutableList<Int>>()
        for (b in buildings) {
            g1.getOrPut(b[0]) { ArrayList() }.add(b[1])
            g2.getOrPut(b[1]) { ArrayList() }.add(b[0])
        }
        for (list in g1.values) { list.sort() }
        for (list in g2.values) { list.sort() }
        var ans = 0
        for (b in buildings) {
            var x = b[0]
            var y = b[1]
            var l1 = g1[x]
            var l2 = g2[y]
            if (l2[0] < x && x < l2[l2.size - 1] && l1[0] < y && y < l1[l1.size - 1]) an{ s = s + 1 }
        }
        return ans
    }
}
