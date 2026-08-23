// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

var recoverOrder = function(order, friends) {
    const n = order.length;
    const d = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) d[order[i]] = i;
    friends.sort((a, b) => d[a] - d[b]);
    return friends;
};
