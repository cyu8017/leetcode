// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

export function checkDistances(s: string, distance: number[]): boolean {
    const first = Array(26).fill(-1);
    for (let i = 0; i < s.length; i++) {
        const c = s.charCodeAt(i) - 97;
        if (first[c] === -1) first[c] = i;
        else if (i - first[c] - 1 !== distance[c]) return false;
    }
    return true;
}
