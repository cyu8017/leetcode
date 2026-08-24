// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

var maxSubtreeInversionSum = function(edges, nums, k) {
    const n = nums.length;
    const graph = Array.from({length: n}, () => []);
    for (const edge of edges) {
        graph[edge[0]].push(edge[1]);
        graph[edge[1]].push(edge[0]);
    }
    const parent = new Array(n).fill(-2);
    parent[0] = -1;
    const order = [0];
    for (let i = 0; i < order.length; i++) {
        const u = order[i];
        for (const v of graph[u]) {
            if (parent[v] === -2) {
                parent[v] = u;
                order.push(v);
            }
        }
    }
    const infinity = 2 ** 60;
    const maximum = new Array(n);
    const minimum = new Array(n);
    for (let oi = n - 1; oi >= 0; oi--) {
        const u = order[oi];
        let currentMax = new Array(k + 1).fill(-infinity);
        let currentMin = new Array(k + 1).fill(infinity);
        currentMax[k] = currentMin[k] = nums[u];
        for (const v of graph[u]) {
            if (parent[v] !== u) continue;
            const nextMax = new Array(k + 1).fill(-infinity);
            const nextMin = new Array(k + 1).fill(infinity);
            for (let first = 0; first <= k; first++) {
                if (currentMax[first] === -infinity) continue;
                for (let childDistance = 0; childDistance <= k; childDistance++) {
                    if (maximum[v][childDistance] === -infinity) continue;
                    let second = childDistance + 1;
                    if (second > k) second = k;
                    if (first < k && second < k && first + second < k) continue;
                    const distance = Math.min(first, second);
                    const maxValue = currentMax[first] + maximum[v][childDistance];
                    const minValue = currentMin[first] + minimum[v][childDistance];
                    nextMax[distance] = Math.max(nextMax[distance], maxValue);
                    nextMin[distance] = Math.min(nextMin[distance], minValue);
                }
            }
            currentMax = nextMax;
            currentMin = nextMin;
        }
        if (-currentMin[k] > currentMax[0]) currentMax[0] = -currentMin[k];
        if (-currentMax[k] < currentMin[0]) currentMin[0] = -currentMax[k];
        maximum[u] = currentMax;
        minimum[u] = currentMin;
    }
    let answer = -(2 ** 60);
    for (const value of maximum[0]) answer = Math.max(answer, value);
    return answer;
};
