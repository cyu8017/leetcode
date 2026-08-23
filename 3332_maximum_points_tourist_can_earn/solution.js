// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

var maxScore = function(n, k, stayScore, travelScore) {
    let dp = new Array(n).fill(0);
    for (let day = 0; day < k; day++) {
        const ndp = new Array(n).fill(-(1 << 30));
        for (let dest = 0; dest < n; dest++) {
            let best = -(1 << 30);
            for (let src = 0; src < n; src++) {
                let val = dp[src];
                if (src === dest) val += stayScore[day][dest];
                else val += travelScore[src][dest];
                if (val > best) best = val;
            }
            ndp[dest] = best;
        }
        dp = ndp;
    }
    let ans = dp[0];
    for (let i = 1; i < n; i++) if (dp[i] > ans) ans = dp[i];
    return ans;
};
