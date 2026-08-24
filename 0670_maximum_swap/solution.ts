// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

export function maximumSwap(num: number): number {
    const digits = String(num).split("");
    const last = Array(10).fill(-1);
    for (let i = 0; i < digits.length; ++i) last[digits[i].charCodeAt(0) - 48] = i;
    for (let i = 0; i < digits.length; ++i) {
        for (let candidate = 9; candidate > digits[i].charCodeAt(0) - 48; --candidate) {
            if (last[candidate] > i) {
                const j = last[candidate];
                [digits[i], digits[j]] = [digits[j], digits[i]];
                return Number(digits.join(""));
            }
        }
    }
    return num;
}
