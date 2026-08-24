// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

export function promisify(fn: Function): Function {
    return function(...args) {
        return new Promise((resolve, reject) => {
            fn((err, result) => {
                if (err) reject(err);
                else resolve(result);
            }, ...args);
        });
    };
}
