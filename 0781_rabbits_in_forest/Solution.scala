// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

object Solution {
  def numRabbits(answers: Array[Int]): Int = {
    val counts = scala.collection.mutable.Map.empty[Int, Int]
    answers.foreach { a => counts(a) = counts.getOrElse(a, 0) + 1 }
    var total = 0
    counts.foreach { case (ans, cnt) =>
      val group = ans + 1
      val groups = (cnt + group - 1) / group
      total += groups * group
    }
    total
  }
}
