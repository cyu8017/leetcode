// LeetCode 1317 - Convert Integer To The Sum Of Two No Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

function getNoZeroIntegers(n: number): number[] {
    const valid = (value: any): any => !String(value).includes("0");
    for (let first = 1; first < n; first++) {
        if (valid(first) && valid(n - first)) return [first, n - first];
    }
    return [];
}
