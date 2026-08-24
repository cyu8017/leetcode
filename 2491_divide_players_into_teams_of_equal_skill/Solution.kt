// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution {
    fun dividePlayers(skill: IntArray): Long {
            skill.sort()
            var n: Int = skill.size
            var target: Int = skill[0] + skill[n - 1]
            var chem: Long = 0
            var i: Int = 0
    while (i < n / 2) {
    
                if (skill[i] + skill[n - 1 - i] != target) return -1
                chem +=1L * skill[i] * skill[n - 1 - i]
    
    i = i + 1
    }
            return chem
    }
}
