"use strict";
function finalPrices(prices) {
    const stack = [];
    for (let i = 0; i < prices.length; i++) {
        while (stack.length && prices[stack[stack.length - 1]] >= prices[i]) {
            prices[stack.pop()] -= prices[i];
        }
        stack.push(i);
    }
    return prices;
}
