// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

import java.util.Arrays;

class Solution {
    public long dividePlayers(int[] skill) {
        Arrays.sort(skill);
        int n = skill.length;
        int target = skill[0] + skill[n - 1];
        long chem = 0;
        for (int i = 0; i < n / 2; i++) {
            if (skill[i] + skill[n - 1 - i] != target) return -1;
            chem += 1L * skill[i] * skill[n - 1 - i];
        }
        return chem;
    }
}
