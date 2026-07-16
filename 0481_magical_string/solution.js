// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

class Solution {
    magicalString(n) {
        if (n === 0) return 0;
        const seq = [1, 2, 2];
        let i = 2;
        while (seq.length < n) {
            if (seq[i] === 1) {
                seq.push(seq[seq.length - 1] === 2 ? 1 : 2);
            } else {
                const value = seq[seq.length - 1] === 2 ? 1 : 2;
                seq.push(value, value);
            }
            i += 1;
        }
        return seq.slice(0, n).filter((value) => value === 1).length;
    }
}

module.exports = { Solution };
