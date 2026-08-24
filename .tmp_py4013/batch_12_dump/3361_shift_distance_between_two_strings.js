// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

var shiftDistance = function(s, t, nextCost, previousCost) {
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        let a = s.charCodeAt(i) - 97, b = t.charCodeAt(i) - 97;
        if (a === b) continue;
        let fwd = 0;
        for (let x = a; x !== b; x = (x + 1) % 26) fwd += nextCost[x];
        let bwd = 0;
        for (let x = a; x !== b; x = (x + 25) % 26) bwd += previousCost[x];
        ans += fwd < bwd ? fwd : bwd;
    }
    return ans;
};
