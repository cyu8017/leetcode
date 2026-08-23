// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

var maxRequests = function(requests, k, window) {
    const g = new Map();
    for (const r of requests) {
        if (!g.has(r[0])) g.set(r[0], []);
        g.get(r[0]).push(r[1]);
    }
    let ans = requests.length;
    for (const ts of g.values()) {
        ts.sort((a, b) => a - b);
        const kept = [];
        for (const t of ts) {
            while (kept.length > 0 && t - kept[0] > window) kept.shift();
            if (kept.length < k) kept.push(t);
            else ans--;
        }
    }
    return ans;
};
