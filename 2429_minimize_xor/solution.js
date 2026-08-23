// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var minimizeXor = function(num1, num2) {
    let bits = 0;
    for (let x = num2; x !== 0; x &= x - 1) bits++;
    let ans = 0;
    for (let i = 31; i >= 0 && bits > 0; i--) {
        if (((num1 >> i) & 1) !== 0) {
            ans |= 1 << i;
            bits--;
        }
    }
    for (let i = 0; i < 32 && bits > 0; i++) {
        if (((ans >> i) & 1) === 0) {
            ans |= 1 << i;
            bits--;
        }
    }
    return ans >>> 0;
};
