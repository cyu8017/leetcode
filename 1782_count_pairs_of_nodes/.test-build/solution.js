"use strict";
// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/
function countPairs(n, edges, queries) {
    const deg = new Array(n + 1).fill(0);
    const shared = new Map();
    for (const edge of edges) {
        let a = edge[0];
        let b = edge[1];
        if (a > b) {
            const tmp = a;
            a = b;
            b = tmp;
        }
        deg[a]++;
        deg[b]++;
        const key = a * 100000 + b;
        shared.set(key, (shared.get(key) || 0) + 1);
    }
    const sortedDeg = deg.slice(1).sort((p, q) => p - q);
    const ans = [];
    for (const q of queries) {
        let res = 0;
        let left = 0;
        let right = n - 1;
        while (left < right) {
            if (sortedDeg[left] + sortedDeg[right] > q) {
                res += right - left;
                right--;
            }
            else {
                left++;
            }
        }
        for (const [key, count] of shared) {
            const a = Math.floor(key / 100000);
            const b = key % 100000;
            const sum = deg[a] + deg[b];
            if (sum > q && q >= sum - count) {
                res--;
            }
        }
        ans.push(res);
    }
    return ans;
}
