// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

export function maxScore(nums: any, maxVal: any): any {
    let limit = maxVal;
    const frequency = new Array(100001).fill(0);
    for (const x of nums) {
        frequency[x]++;
        if (x > limit) limit = x;
    }
    const divisible = new Array(limit + 1).fill(0);
    for (let d = 1; d <= limit; d++) {
        for (let multiple = d; multiple <= limit; multiple += d) {
            if (multiple < frequency.length) divisible[d] += frequency[multiple];
        }
    }
    let best = -nums.length;
    const checked = new Array(limit + 1).fill(false);
    for (let x = 1; x <= maxVal; x++) {
        best = Math.max(best, evaluate(x, x < frequency.length && frequency[x] > 0, checked, divisible));
    }
    for (const x of nums) {
        best = Math.max(best, evaluate(x, true, checked, divisible));
    }
    return best;
}
function evaluate(x: any, exists: any, checked: any, divisible: any): any {
    if (checked[x]) return Math.floor(-2147483648 / 4);
    checked[x] = true;
    const bad = badCount(x, divisible);
    let cost;
    if (exists) cost = x > 1 ? bad - 1 : 0;
    else cost = bad > 0 ? bad : 1;
    return x - cost;
}
function badCount(x: any, divisible: any): any {
    const primes = [];
    let y = x;
    for (let p = 2; p * p <= y; p++) {
        if (y % p === 0) {
            primes.push(p);
            while (y % p === 0) y = Math.floor(y / p);
        }
    }
    if (y > 1) primes.push(y);
    let bad = 0;
    const psz = primes.length;
    for (let mask = 1; mask < (1 << psz); mask++) {
        let product = 1, bits = 0;
        for (let i = 0; i < psz; i++) {
            if (((mask >> i) & 1) !== 0) {
                product *= primes[i];
                bits++;
            }
        }
        if (bits % 2 === 1) bad += divisible[product];
        else bad -= divisible[product];
    }
    return bad;
}
