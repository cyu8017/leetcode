// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

var maximumCoins = function(coins, k) {
    coins = coins.slice().sort((a, b) => a[0] - b[0]);
    let ans = 0;
    const n = coins.length;
    for (let i = 0; i < n; i++) {
        let sum = 0;
        const start = coins[i][0];
        const end = start + k - 1;
        for (let j = i; j < n && coins[j][0] <= end; j++) {
            let l = coins[j][0];
            let r = coins[j][1];
            if (r > end) r = end;
            if (l < start) l = start;
            if (l <= r) sum += (r - l + 1) * coins[j][2];
        }
        if (sum > ans) ans = sum;
    }
    for (let i = 0; i < n; i++) {
        let sum = 0;
        const end = coins[i][1];
        const start = end - k + 1;
        for (let j = 0; j <= i; j++) {
            let l = coins[j][0];
            let r = coins[j][1];
            if (l < start) l = start;
            if (r > end) r = end;
            if (l <= r) sum += (r - l + 1) * coins[j][2];
        }
        if (sum > ans) ans = sum;
    }
    return ans;
};
