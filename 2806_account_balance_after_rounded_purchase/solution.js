// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

/**
 * @param {number} purchaseAmount
 * @return {number}
 */
var accountBalanceAfterPurchase = function(purchaseAmount) {
    const r = Math.floor((purchaseAmount + 5) / 10) * 10;
    return 100 - r;
};
