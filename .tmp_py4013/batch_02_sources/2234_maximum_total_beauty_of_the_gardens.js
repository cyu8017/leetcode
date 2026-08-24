// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

/**
 * @param {number[]} flowers
 * @param {number} newFlowers
 * @param {number} target
 * @param {number} full
 * @param {number} partial
 * @return {number}
 */
var maximumBeauty = function(flowers, newFlowers, target, full, partial) {
    const n = flowers.length;
    for (let i = 0; i < n; i++) if (flowers[i] > target) flowers[i] = target;
    flowers.sort((a, b) => a - b);
    let sum = 0;
    for (const f of flowers) sum += f;
    if (target * n - sum <= newFlowers) return n * full;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + flowers[i];
    let ans = 0;
    let j = n - 1;
    let remain = newFlowers;
    for (let complete = 0; complete <= n; complete++) {
        if (complete > 0) {
            const need = target - flowers[n - complete];
            if (remain < need) break;
            remain -= need;
        }
        while (j >= n - complete || (j >= 0 && flowers[j] * (j + 1) - pref[j + 1] > remain)) j--;
        let partialVal = 0;
        if (j >= 0) {
            const extra = Math.floor((remain - (flowers[j] * (j + 1) - pref[j + 1])) / (j + 1));
            partialVal = flowers[j] + extra;
            if (partialVal >= target) partialVal = target - 1;
        }
        ans = Math.max(ans, complete * full + partialVal * partial);
    }
    return ans;
};
