// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

class Solution {
    fun maxArea(height: Int, positions: IntArray, directions: String): Long {
        var n = positions.size
        var pos = positions.clone()
        var dir = directions.toCharArray()
        var best = 0
        for (t in 0 ..2 * height) {
            var sum = 0
            for (i in 0 until n) { sum += pos[i] }
            if (sum > best) best = sum
            for (i in 0 until n) {
                if (dir[i] == 'U') {
                    if (pos[i] == height) { dir[i] = 'D'; pos[i]--; }
                    else pos[i]++
                } else {
                    if (pos[i] == 0) { dir[i] = 'U'; pos[i]++; }
                    else pos[i]--
                }
            }
        }
        return best
    }
}
