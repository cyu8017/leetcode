// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

export function reorderedPowerOf2(n: number): boolean {
    const sig = (x) => String(x).split('').sort().join('');
    const target = sig(n);
    for (let i = 0; i < 31; i++) if (sig(1 << i) === target) return true;
    return false;
}
