// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

/**
 * @param {number} left
 * @param {number} right
 * @return {string}
 */
var abbreviateProduct = function(left, right) {
    let twos = 0, fives = 0;
    for (let i = left; i <= right; i++) {
        let x = i;
        while (x % 2 === 0) { twos++; x = Math.floor(x / 2); }
        while (x % 5 === 0) { fives++; x = Math.floor(x / 5); }
    }
    const zeros = Math.min(twos, fives);
    const MOD = 100000000000;
    let prod = 1;
    let extra2 = twos - zeros, extra5 = fives - zeros;
    let logSum = 0.0;
    for (let i = left; i <= right; i++) {
        let x = i;
        while (x % 2 === 0) x = Math.floor(x / 2);
        while (x % 5 === 0) x = Math.floor(x / 5);
        prod = Number((BigInt(prod) * BigInt(x)) % BigInt(MOD));
        logSum += Math.log10(x);
    }
    for (let i = 0; i < extra2; i++) { prod = Number((BigInt(prod) * 2n) % BigInt(MOD)); logSum += Math.log10(2.0); }
    for (let i = 0; i < extra5; i++) { prod = Number((BigInt(prod) * 5n) % BigInt(MOD)); logSum += Math.log10(5.0); }
    let fullLog = 0.0;
    for (let i = left; i <= right; i++) fullLog += Math.log10(i);
    const digits = Math.floor(fullLog) + 1;
    if (digits <= 10) {
        let p = 1n;
        for (let i = left; i <= right; i++) p *= BigInt(i);
        return p.toString();
    }
    const frac = logSum - Math.floor(logSum);
    const prefix = Math.floor(Math.pow(10.0, frac + 4));
    const suffix = prod % 100000;
    return prefix + "e" + zeros + String(suffix).padStart(5, '0');
};
