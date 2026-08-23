// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

var partitionString = function(s) {
    const vis = new Set();
    const ans = [];
    let t = '';
    for (const c of s) {
        t += c;
        if (!vis.has(t)) {
            vis.add(t);
            ans.push(t);
            t = '';
        }
    }
    return ans;
};
