// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
// @ts-nocheck

function maxUniqueSplit(s: string): number {
    const used = new Set();
    let answer = 0;
    const dfs = (i) => {
        if (used.size + s.length - i <= answer) return;
        if (i === s.length) {
            answer = Math.max(answer, used.size);
            return;
        }
        for (let j = i + 1; j <= s.length; j++) {
            const part = s.slice(i, j);
            if (!used.has(part)) {
                used.add(part);
                dfs(j);
                used.delete(part);
            }
        }
    };
    dfs(0);
    return answer;
}
