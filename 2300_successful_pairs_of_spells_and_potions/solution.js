// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

var successfulPairs = function(spells, potions, success) {
    potions.sort((a, b) => a - b);
    const m = potions.length;
    const ans = new Array(spells.length);
    for (let i = 0; i < spells.length; i++) {
        let lo = 0, hi = m;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (spells[i] * potions[mid] >= success) hi = mid;
            else lo = mid + 1;
        }
        ans[i] = m - lo;
    }
    return ans;
};
