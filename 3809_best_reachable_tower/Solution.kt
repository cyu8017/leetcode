// LeetCode 3809 - Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/

class Solution {
    fun bestTower(towers: Array<IntArray>, center: IntArray, radius: Int): IntArray {
        var cx = center[0]
        var cy = center[1]
        var idx = -1
        for (i in 0 until towers.size) {
            var x = towers[i][0]
            var y = towers[i][1]
            var q = towers[i][2]
            var dist = kotlin.math.abs(x - cx) + kotlin.math.abs(y - cy)
            if (dist > radius) continue
            if (idx == -1 || towers[idx][2] < q ||
                (towers[idx][2] == q &&
                 (x < towers[idx][0] || (x == towers[idx][0] && y < towers[idx][1])))) {
                idx = i
            }
        }
        if (idx == -1) return intArrayOf( -1, -1 )
        return intArrayOf( towers[idx][0], towers[idx][1] )
    }
}
