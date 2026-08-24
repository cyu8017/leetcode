// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

export function countCoveredBuildings(n: any, buildings: any): any {
    const g1 = new Map(), g2 = new Map();
    for (const b of buildings) {
        if (!g1.has(b[0])) g1.set(b[0], []);
        if (!g2.has(b[1])) g2.set(b[1], []);
        g1.get(b[0]).push(b[1]);
        g2.get(b[1]).push(b[0]);
    }
    for (const list of g1.values()) list.sort((a, b) => a - b);
    for (const list of g2.values()) list.sort((a, b) => a - b);
    let ans = 0;
    for (const b of buildings) {
        const x = b[0], y = b[1];
        const l1 = g1.get(x), l2 = g2.get(y);
        if (l2[0] < x && x < l2[l2.length - 1] && l1[0] < y && y < l1[l1.length - 1]) ans++;
    }
    return ans;
}
