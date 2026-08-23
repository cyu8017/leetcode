// LeetCode 0476 - Number Complement
// https://leetcode.com/problems/number-complement/

class Solution {
    findComplement(num) {
        let mask = num;
        mask |= mask >> 1;
        mask |= mask >> 2;
        mask |= mask >> 4;
        mask |= mask >> 8;
        mask |= mask >> 16;
        return num ^ mask;
    }
}

module.exports = { Solution };
