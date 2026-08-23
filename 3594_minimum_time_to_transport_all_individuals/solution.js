// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

var minTime = function(n, k, m, time, mul) {
    const t = time.slice().sort((a, b) => a - b);
    let total = 0;
    let stage = 0, left = n;
    while (left > 0) {
        const take = Math.min(k, left);
        const slow = t[left - 1];
        total += slow * mul[stage % m];
        left -= take;
        stage++;
        if (left > 0) {
            total += t[0] * mul[stage % m];
            stage++;
        }
    }
    return total;
};
