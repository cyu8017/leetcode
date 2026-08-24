// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

export function crackSafe(n: number, k: number): string {
    const seen = new Set();
    const path = [];
    let start = '';
    for (let i = 0; i < n - 1; i++) start += '0';
    const dfs = (node) => {
        for (let d = 0; d < k; d++) {
            const digit = String(d);
            const edge = node + digit;
            if (!seen.has(edge)) {
                seen.add(edge);
                dfs(edge.substring(1));
                path.push(digit);
            }
        }
    };
    dfs(start);
    return path.join('') + start;
}
