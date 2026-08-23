// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

var largestGoodInteger = function(num) {
    let best = '';
    for (let i = 0; i + 2 < num.length; i++) {
        if (num[i] === num[i + 1] && num[i] === num[i + 2]) {
            const cand = num.slice(i, i + 3);
            if (cand > best) best = cand;
        }
    }
    return best;
};
