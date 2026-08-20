// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

function mostVisitedPattern(username: string[], timestamp: number[], website: string[]): string[] {
    const visits = new Map();
    for (let i = 0; i < username.length; i++) {
        if (!visits.has(username[i])) visits.set(username[i], []);
        visits.get(username[i]).push([timestamp[i], website[i]]);
    }
    const scores = new Map();
    for (const entries of visits.values()) {
        const sites = entries.sort((a, b) => a[0] - b[0]).map((e) => e[1]);
        const patterns = new Set();
        for (let i = 0; i < sites.length; i++) {
            for (let j = i + 1; j < sites.length; j++) {
                for (let k = j + 1; k < sites.length; k++) {
                    patterns.add(`${sites[i]},${sites[j]},${sites[k]}`);
                }
            }
        }
        for (const p of patterns) scores.set(p, (scores.get(p) || 0) + 1);
    }
    let best = null, bestCount = -1;
    for (const [pattern, count] of scores) {
        if (count > bestCount || (count === bestCount && pattern < best)) {
            bestCount = count;
            best = pattern;
        }
    }
    return best.split(",");
}
