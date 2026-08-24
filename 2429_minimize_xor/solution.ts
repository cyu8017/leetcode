// LeetCode 2429 - Minimize XOR
// https://leetcode.com/problems/minimize-xor/

export function minimizeXor(num1: number, num2: number): number {
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
}
