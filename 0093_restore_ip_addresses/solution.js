// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    const result = [];
    const path = [];

    function backtrack(start) {
        if (path.length === 4) {
            if (start === s.length) {
                result.push(path.join('.'));
            }
            return;
        }

        for (let length = 1; length <= 3; length++) {
            if (start + length > s.length) {
                break;
            }
            const part = s.substring(start, start + length);
            if ((part.startsWith('0') && part.length > 1) || parseInt(part, 10) > 255) {
                continue;
            }
            path.push(part);
            backtrack(start + length);
            path.pop();
        }
    }

    backtrack(0);
    return result;
};
