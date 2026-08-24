// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

export function distinctNames(ideas: string[]): number {
    const groups = Array.from({ length: 26 }, () => new Set());
    for (const idea of ideas) groups[idea.charCodeAt(0) - 97].add(idea.substring(1));
    let ans = 0;
    for (let i = 0; i < 26; ++i) {
        for (let j = i + 1; j < 26; ++j) {
            let overlap = 0;
            for (const s of groups[i]) if (groups[j].has(s)) overlap++;
            ans += (groups[i].size - overlap) * (groups[j].size - overlap) * 2;
        }
    }
    return ans;
}
