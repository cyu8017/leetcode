// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

/**
 * @param {string} binary
 * @return {string}
 */
var maximumBinaryString = function(binary) {
    let zeros = 0;
    for (const ch of binary) {
        if (ch === '0') {
            zeros++;
        }
    }
    if (zeros <= 1) {
        return binary;
    }
    const first = binary.indexOf('0');
    const n = binary.length;
    return '1'.repeat(first + zeros - 1) + '0' + '1'.repeat(n - first - zeros);
};
