// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

impl Solution {
    pub fn divide_players(mut skill: Vec<i32>) -> i64 {
        skill.sort_unstable();
        let n = skill.len();
        let target = skill[0] + skill[n - 1];
        let mut chem = 0i64;
        for i in 0..n / 2 {
            if skill[i] + skill[n - 1 - i] != target {
                return -1;
            }
            chem += skill[i] as i64 * skill[n - 1 - i] as i64;
        }
        chem
    }
}
