// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

var maxPossibleScore = function(start, d) {
    start.sort((a, b) => a - b);
    const n = start.length;
    const ok = (mid) => {
        let prev = start[0];
        for (let i = 1; i < start.length; i++) {
            const need = prev + mid;
            const cur = start[i];
            if (need > cur + d) return false;
            prev = need > cur ? need : cur;
        }
        return true;
    };
    let lo = 0, hi = start[n - 1] + d - start[0] + 1;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (ok(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
