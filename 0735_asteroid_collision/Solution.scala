// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

object Solution {
  def asteroidCollision(asteroids: Array[Int]): Array[Int] = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (asteroid <- asteroids) {
      var alive = true
      while (alive && stack.nonEmpty && asteroid < 0 && stack.last > 0) {
        if (stack.last < -asteroid) {
          stack.remove(stack.length - 1)
        } else {
          if (stack.last == -asteroid) stack.remove(stack.length - 1)
          alive = false
        }
      }
      if (alive) stack += asteroid
    }
    stack.toArray
  }
}
