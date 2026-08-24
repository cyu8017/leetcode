// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

export function debounce(fn: any, t: any): any {
    let timer = null;
    return function(...args) {
        if (timer !== null) clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    };
}
