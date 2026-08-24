// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    let bestLen = 0, bestNodes = 1;
    const dfs = (u, p, dist, pathVals, pathDist) => {
        pathVals.push(nums[u]);
        pathDist.push(dist);
        const freq = new Map();
        let dups = 0, left = 0;
        for (let right = 0; right < pathVals.length; right++) {
            const v = pathVals[right];
            freq.set(v, (freq.get(v) || 0) + 1);
            if (freq.get(v) === 2) dups++;
            while (dups > 1) {
                const lv = pathVals[left];
                if (freq.get(lv) === 2) dups--;
                freq.set(lv, freq.get(lv) - 1);
                left++;
            }
        }
        const length = dist - pathDist[left];
        const nodes = pathVals.length - left;
        if (length > bestLen || (length === bestLen && nodes < bestNodes)) {
            bestLen = length;
            bestNodes = nodes;
        }
        for (const e of g[u]) {
            if (e[0] === p) continue;
            dfs(e[0], u, dist + e[1], pathVals, pathDist);
        }
        pathVals.pop();
        pathDist.pop();
    };
    dfs(0, -1, 0, [], []);
    return [bestLen, bestNodes];
};
