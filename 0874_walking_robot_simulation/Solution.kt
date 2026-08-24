// LeetCode 0874 - Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/

class Solution {
    fun robotSim(commands: IntArray, obstacles: Array<IntArray>): Int {
        var blocked = HashSet<Long>()
        for (o in obstacles) { blocked.add(encode(o[0], o[1])) }
        var dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
        var x = 0
        var y = 0
        var d = 0
        var best = 0
        for (cmd in commands) {
            if (cmd == -1) d = (d + 1) % 4
            else if (cmd == -2) d = (d + 3) % 4
            else {
                var dx = dirs[d][0]
                var dy = dirs[d][1]
                for (step in 0 until cmd) {
                    var nx = x + dx
                    var ny = y + dy
                    if (blocked.contains(encode(nx, ny))) break
                    x = nx
                    y = ny
                }
                best = maxOf(best, x * x + y * y)
            }
        }
        return best
    }

    private fun encode(x: Int, y: Int): Long {
        return ((x + 30000)  shl  20) | (y + 30000)
    }
}
