// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long dividePlayers(int* skill, int skillSize) {
    qsort(skill, (size_t)skillSize, sizeof(int), cmp_int);
    int n = skillSize;
    int target = skill[0] + skill[n - 1];
    long long chem = 0;
    for (int i = 0; i < n / 2; i++) {
        if (skill[i] + skill[n - 1 - i] != target) return -1;
        chem += (long long)skill[i] * skill[n - 1 - i];
    }
    return chem;
}
