// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var minInteger = function(num, k) {
    const n = num.length;
    const bit = Array(n + 1).fill(0);
    const add = (i, delta) => {
        for (i += 1; i < bit.length; i += i & -i) bit[i] += delta;
    };
    const sum = (i) => {
        let out = 0;
        while (i > 0) {
            out += bit[i];
            i -= i & -i;
        }
        return out;
    };
    const positions = Array.from({ length: 10 }, () => []);
    for (let i = 0; i < n; i++) positions[+num[i]].push(i);
    const heads = Array(10).fill(0);
    const out = [];
    for (let t = 0; t < n; t++) {
        for (let digit = 0; digit < 10; digit++) {
            if (heads[digit] >= positions[digit].length) continue;
            const index = positions[digit][heads[digit]];
            const cost = index - sum(index);
            if (cost <= k) {
                k -= cost;
                heads[digit]++;
                add(index, 1);
                out.push(String(digit));
                break;
            }
        }
    }
    return out.join("");
};
