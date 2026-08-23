// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

var debounce = function(fn, t) {
    let timer = null;
    return function(...args) {
        if (timer !== null) clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    };
};
