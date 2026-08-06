// LeetCode 1306 - Jump Game III
// https://leetcode.com/problems/jump-game-iii/

object Solution {
  def canReach(arr: Array[Int], start: Int): Boolean = {
    val stack = scala.collection.mutable.ArrayDeque[Int]()
    val seen = scala.collection.mutable.HashSet[Int]()
    stack.append(start)
    while (stack.nonEmpty) {
      val i = stack.removeLast()
      if (!seen.contains(i) && i >= 0 && i < arr.length) {
        if (arr(i) == 0) return true
        seen += i
        stack.append(i - arr(i))
        stack.append(i + arr(i))
      }
    }
    false
  }
}
