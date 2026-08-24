// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

object Solution {
  def flipgame(fronts: Array[Int], backs: Array[Int]): Int = {
    val same = scala.collection.mutable.Set.empty[Int]
    fronts.indices.foreach { i => if (fronts(i) == backs(i)) same += fronts(i) }
    var best = Int.MaxValue
    fronts.foreach { x => if (!same.contains(x)) best = math.min(best, x) }
    backs.foreach { x => if (!same.contains(x)) best = math.min(best, x) }
    if (best == Int.MaxValue) 0 else best
  }
}
