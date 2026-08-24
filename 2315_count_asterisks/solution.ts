// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

export function countAsterisks(s: string): number {
    let ans = 0, inside = false;
    for (const c of s) {
        if (c === '|') inside = !inside;
        else if (c === '*' && !inside) ans++;
    }
    return ans;
}
