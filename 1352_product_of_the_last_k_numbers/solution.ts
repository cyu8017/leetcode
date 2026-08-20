// LeetCode 1352 - Product Of The Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers {
    p: any;
    constructor() {

        this.p = [1];
    }
    add(num: number): void {

        if (num === 0) this.p = [1];
        else this.p.push(this.p[this.p.length - 1] * num);
    }
    getProduct(k: number): number {

        if (k >= this.p.length) return 0;
        return this.p[this.p.length - 1] / this.p[this.p.length - 1 - k];
    }
}
