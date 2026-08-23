// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

/**
 * @param {number} money
 * @param {number} children
 * @return {number}
 */
var distMoney = function(money, children) {
    if (money < children) return -1;
    money -= children;
    let ans = Math.floor(money / 7);
    if (ans > children) ans = children;
    const remainMoney = money - ans * 7;
    const remainChild = children - ans;
    if (remainChild === 0 && remainMoney > 0) ans--;
    else if (remainChild === 1 && remainMoney === 3) ans--;
    if (ans < 0) return 0;
    return ans;
};
