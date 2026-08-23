// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

var doesValidArrayExist = function(derived) {
    let x = 0;
    for (const v of derived) x ^= v;
    return x === 0;
};
