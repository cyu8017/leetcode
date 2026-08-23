// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

var minimumAddedCoins = function(coins, target) {
    coins.sort((a, b) => a - b);
    let ans = 0, reach = 0, i = 0;
    while (reach < target) {
        if (i < coins.length && coins[i] <= reach + 1) {
            reach += coins[i];
            i++;
        } else {
            reach += reach + 1;
            ans++;
        }
    }
    return ans;
};
