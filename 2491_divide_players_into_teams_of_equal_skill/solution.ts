// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

export function dividePlayers(skill: number[]): number {
    skill = skill.slice().sort((a, b) => a - b);
    const n = skill.length;
    const target = skill[0] + skill[n - 1];
    let chem = 0;
    for (let i = 0; i < n / 2; i++) {
        if (skill[i] + skill[n - 1 - i] !== target) return -1;
        chem += skill[i] * skill[n - 1 - i];
    }
    return chem;
}
