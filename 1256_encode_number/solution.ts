// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

function encode(num: number): string {
    return (num + 1).toString(2).slice(1);
}
