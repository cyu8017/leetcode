// LeetCode 1352 - Product Of The Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

var ProductOfNumbers = function() {
    this.p = [1];
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    if (num === 0) this.p = [1];
    else this.p.push(this.p[this.p.length - 1] * num);
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    if (k >= this.p.length) return 0;
    return this.p[this.p.length - 1] / this.p[this.p.length - 1 - k];
};
