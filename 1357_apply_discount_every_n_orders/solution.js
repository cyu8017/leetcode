// LeetCode 1357 - Apply Discount Every N Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

/**
 * @param {number} n
 * @param {number} discount
 * @param {number[]} products
 * @param {number[]} prices
 */
var Cashier = function(n, discount, products, prices) {
    this.n = n;
    this.discount = discount;
    this.price = new Map();
    for (let i = 0; i < products.length; i++) this.price.set(products[i], prices[i]);
    this.count = 0;
};

/** 
 * @param {number[]} product 
 * @param {number[]} amount
 * @return {number}
 */
Cashier.prototype.getBill = function(product, amount) {
    this.count++;
    let total = 0;
    for (let i = 0; i < product.length; i++) total += this.price.get(product[i]) * amount[i];
    return this.count % this.n === 0 ? total * (100 - this.discount) / 100 : total;
};
