// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

object Solution {
  def smallestSufficientTeam(req_skills: Array[String], people: List[List[String]]): Array[Int] = {
    val n = req_skills.length
    val skillIndex = req_skills.zipWithIndex.toMap
    val peopleMask = people.map(p => p.map(skillIndex).foldLeft(0)((acc, i) => acc | (1 << i))).toArray
    val dp = Array.fill[Array[Int]](1 << n)(null)
    dp(0) = Array.empty[Int]
    for (mask <- 0 until (1 << n) if dp(mask) != null; i <- peopleMask.indices) {
      val next = mask | peopleMask(i)
      if (dp(next) == null || dp(next).length > dp(mask).length + 1) {
        dp(next) = dp(mask) :+ i
      }
    }
    dp((1 << n) - 1)
  }
}
