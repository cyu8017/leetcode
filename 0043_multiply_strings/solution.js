// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    if (num1 === "0" || num2 === "0") {
        return "0";
    }

    const positions = new Array(num1.length + num2.length).fill(0);

    for (let i = num1.length - 1; i >= 0; i -= 1) {
        for (let j = num2.length - 1; j >= 0; j -= 1) {
            const product = Number(num1[i]) * Number(num2[j]);
            const low = i + j + 1;
            const high = i + j;
            const total = product + positions[low];
            positions[low] = total % 10;
            positions[high] += Math.floor(total / 10);
        }
    }

    const result = positions.join("").replace(/^0+/, "");
    return result || "0";
};
