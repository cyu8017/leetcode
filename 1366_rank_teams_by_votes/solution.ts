// LeetCode 1366 - Rank Teams By Votes
// https://leetcode.com/problems/rank-teams-by-votes/

function rankTeams(votes: string[]): string {
    const m = votes[0].length;
    const count = new Map();
    for (const c of votes[0]) count.set(c, Array(m).fill(0));
    for (const v of votes) {
        for (let i = 0; i < v.length; i++) count.get(v[i])[i]++;
    }
    return [...count.keys()].sort((a, b: any): any => {
        const ca = count.get(a), cb = count.get(b);
        for (let i = 0; i < m; i++) if (ca[i] !== cb[i]) return cb[i] - ca[i];
        return a < b ? -1 : a > b ? 1 : 0;
    }).join("");
}
