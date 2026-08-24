// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

object Solution {
  def dividePlayers(skill: Array[Int]): Long = {
    scala.util.Sorting.quickSort(skill)
    val n = skill.length
    val target = skill(0) + skill(n - 1)
    var chem = 0L
    var i = 0
    while (i < n / 2) {
      if (skill(i) + skill(n - 1 - i) != target) return -1
      chem += skill(i).toLong * skill(n - 1 - i)
      i += 1
    }
    chem
  }
}
