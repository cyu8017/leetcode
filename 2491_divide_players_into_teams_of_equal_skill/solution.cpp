// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long dividePlayers(std::vector<int>& skill) {
        std::sort(skill.begin(), skill.end());
        int n = (int)skill.size();
        int target = skill[0] + skill[n - 1];
        long long chem = 0;
        for (int i = 0; i < n / 2; i++) {
            if (skill[i] + skill[n - 1 - i] != target) return -1;
            chem += 1LL * skill[i] * skill[n - 1 - i];
        }
        return chem;
    }
};
