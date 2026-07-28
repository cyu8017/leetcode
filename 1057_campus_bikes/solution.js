// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

/**
 * @param {number[][]} workers
 * @param {number[][]} bikes
 * @return {number[]}
 */
var assignBikes = function(workers, bikes) {
    const triples = [];
    for (let w = 0; w < workers.length; w++) {
        const [wx, wy] = workers[w];
        for (let b = 0; b < bikes.length; b++) {
            const [bx, by] = bikes[b];
            triples.push([Math.abs(wx - bx) + Math.abs(wy - by), w, b]);
        }
    }
    triples.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
    const ans = new Array(workers.length).fill(-1);
    const usedBikes = new Set();
    let assigned = 0;
    for (const [, w, b] of triples) {
        if (ans[w] === -1 && !usedBikes.has(b)) {
            ans[w] = b;
            usedBikes.add(b);
            assigned++;
            if (assigned === workers.length) break;
        }
    }
    return ans;
};
