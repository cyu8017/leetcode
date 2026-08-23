// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

var maxItems = function(items, budget) {
    const n = items.length;
    const frequency = new Array(n + 1).fill(0);
    let minimumPrice = items[0][1];
    for (const item of items) {
        frequency[item[0]]++;
        minimumPrice = Math.min(minimumPrice, item[1]);
    }
    const batches = [];
    for (const item of items) {
        let gain = 0;
        for (let multiple = item[0]; multiple <= n; multiple += item[0]) gain += frequency[multiple];
        gain--;
        if (gain > 0 && item[1] < 2 * minimumPrice) batches.push([item[1], gain]);
    }
    batches.sort((a, b) => a[0] - b[0]);
    let remaining = budget;
    let answer = Math.floor(budget / minimumPrice);
    let boosted = 0;
    for (const current of batches) {
        let count = current[1];
        const affordable = Math.floor(remaining / current[0]);
        if (affordable < count) count = affordable;
        remaining -= count * current[0];
        boosted += count;
        const total = 2 * boosted + Math.floor(remaining / minimumPrice);
        if (total > answer) answer = total;
        if (count < current[1]) break;
    }
    return answer;
};
