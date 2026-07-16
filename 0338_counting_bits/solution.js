// LeetCode 0338 - Counting Bits
var countBits = function(n) {
    const result = new Array(n + 1).fill(0);
    for (let index = 1; index <= n; index += 1) {
        result[index] = result[index & (index - 1)] + 1;
    }
    return result;
};
