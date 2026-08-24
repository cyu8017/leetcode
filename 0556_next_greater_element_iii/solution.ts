// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

export function nextGreaterElement(n: number): number {
    const digits = String(n).split("");
    let i = digits.length - 2;
    while (i >= 0 && digits[i] >= digits[i + 1]) --i;
    if (i < 0) return -1;
    let j = digits.length - 1;
    while (digits[j] <= digits[i]) --j;
    [digits[i], digits[j]] = [digits[j], digits[i]];
    let left = i + 1, right = digits.length - 1;
    while (left < right) {
        [digits[left], digits[right]] = [digits[right], digits[left]];
        ++left;
        --right;
    }
    const value = Number(digits.join(""));
    return value > 2147483647 ? -1 : value;
}
