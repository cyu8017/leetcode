// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

import scala.collection.mutable

trait Robot {
  def move(): Boolean
  def turnLeft(): Unit
  def turnRight(): Unit
  def clean(): Unit
}

object Solution {
  private val directions = Array(Array(-1, 0), Array(0, 1), Array(1, 0), Array(0, -1))

  def cleanRoom(robot: Robot): Unit = {
    val visited = mutable.Set("0,0,0")
    backtrack(robot, 0, 0, 0, visited)
  }

  private def backtrack(robot: Robot, row: Int, col: Int, direction: Int, visited: mutable.Set[String]): Unit = {
    robot.clean()
    for (step <- 0 until 4) {
      val d = (direction + step) % 4
      val nextRow = row + directions(d)(0)
      val nextCol = col + directions(d)(1)
      val key = s"$nextRow,$nextCol,$d"
      if (!visited.contains(key) && robot.move()) {
        visited.add(key)
        backtrack(robot, nextRow, nextCol, d, visited)
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
