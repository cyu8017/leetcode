// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution {
    func dividePlayers(_ skill: [Int]) -> Int {
        let skill = skill.sorted()
        let n = skill.count
        let target = skill[0] + skill[n - 1]
        var chem = 0
        for i in 0..<(n / 2) {
            if skill[i] + skill[n - 1 - i] != target { return -1 }
            chem += skill[i] * skill[n - 1 - i]
        }
        return chem
    }
}
