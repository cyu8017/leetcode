// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var kMirror = function(k, n) {
    const isPalBase = (x, bas) => {
        const digits = [];
        while (x > 0) { digits.push(x % bas); x = Math.floor(x / bas); }
        for (let l = 0, r = digits.length - 1; l < r; l++, r--)
            if (digits[l] !== digits[r]) return false;
        return true;
    };
    let ans = 0, count = 0;
    for (let length = 1; count < n; length++) {
        let start = 1;
        for (let i = 1; i < Math.floor((length + 1) / 2); i++) start *= 10;
        const end = start * 10;
        for (let half = start; half < end && count < n; half++) {
            let pal = half;
            if (length % 2 === 0) {
                let x = half;
                while (x > 0) { pal = pal * 10 + x % 10; x = Math.floor(x / 10); }
            } else {
                let x = Math.floor(half / 10);
                while (x > 0) { pal = pal * 10 + x % 10; x = Math.floor(x / 10); }
            }
            if (isPalBase(pal, k)) { ans += pal; count++; }
        }
    }
    return ans;
};
