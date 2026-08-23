// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

/**
 * @param {number[]} count
 * @param {number[]} upgrade
 * @param {number[]} sell
 * @param {number[]} money
 * @return {number[]}
 */
var maxUpgrades = function(count, upgrade, sell, money) {
    const ans = new Array(count.length);
    for (let i = 0; i < count.length; i++) {
        const cnt = count[i];
        ans[i] = Math.min(cnt, Math.floor((cnt * sell[i] + money[i]) / (upgrade[i] + sell[i])));
    }
    return ans;
};
