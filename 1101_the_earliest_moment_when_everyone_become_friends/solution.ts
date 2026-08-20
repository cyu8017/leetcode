// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

function earliestAcq(logs: number[][], n: number): number {
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const union = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra === rb) return false;
        parent[rb] = ra;
        return true;
    };
    logs.sort((a, b) => a[0] - b[0]);
    let components = n;
    for (const [t, a, b] of logs) {
        if (union(a, b)) {
            components--;
            if (components === 1) return t;
        }
    }
    return -1;
}
