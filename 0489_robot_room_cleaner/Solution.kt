// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

interface Robot {
    fun move(): Boolean
    fun turnLeft()
    fun turnRight()
    fun clean()
}

class Solution {
    private val directions = arrayOf(intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(1, 0), intArrayOf(0, -1))
    private val visited = mutableSetOf<String>()

    fun cleanRoom(robot: Robot) {
        visited.add("0,0,0")
        backtrack(robot, 0, 0, 0)
    }

    private fun backtrack(robot: Robot, row: Int, col: Int, direction: Int) {
        robot.clean()
        for (step in 0 until 4) {
            val d = (direction + step) % 4
            val nextRow = row + directions[d][0]
            val nextCol = col + directions[d][1]
            val key = "$nextRow,$nextCol,$d"
            if (key !in visited && robot.move()) {
                visited.add(key)
                backtrack(robot, nextRow, nextCol, d)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            }
            robot.turnRight()
        }
    }
}
