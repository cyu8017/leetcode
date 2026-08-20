// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

function smallestSufficientTeam(req_skills: string[], people: string[][]): number[] {
    const skillId = new Map(req_skills.map((s, i) => [s, i]));
    const personMasks = people.map((skills) => {
        let mask = 0;
        for (const skill of skills) mask |= 1 << skillId.get(skill);
        return mask;
    });
    const target = (1 << req_skills.length) - 1;
    const n = people.length;
    const dp = Array(1 << req_skills.length).fill(null);
    dp[0] = [];
    for (let state = 0; state <= target; state++) {
        if (!dp[state]) continue;
        for (let i = 0; i < n; i++) {
            const next = state | personMasks[i];
            if (next === state) continue;
            const team = dp[state].concat(i);
            if (!dp[next] || team.length < dp[next].length) dp[next] = team;
        }
    }
    return dp[target];
}
