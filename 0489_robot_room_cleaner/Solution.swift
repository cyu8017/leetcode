// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

class Solution {
    func cleanRoom(_ robot: Robot) {
        var visited: Set<String> = []
        let directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        func backtrack(_ row: Int, _ col: Int, _ direction: Int) {
            robot.clean()
            for step in 0..<4 {
                let d = (direction + step) % 4
                let (dr, dc) = directions[d]
                let nextRow = row + dr
                let nextCol = col + dc
                let key = "\(nextRow),\(nextCol),\(d)"
                if !visited.contains(key) && robot.move() {
                    visited.insert(key)
                    backtrack(nextRow, nextCol, d)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                }
                robot.turnRight()
            }
        }

        visited.insert("0,0,0")
        backtrack(0, 0, 0)
    }
}

/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 */
protocol Robot {
    func move() -> Bool
    func turnLeft()
    func turnRight()
    func clean()
}
