// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

function modPow(a, b, mod) {
    let res = 1 % mod;
    a %= mod;
    while (b > 0) {
        if ((b & 1) !== 0) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}
var getGoodIndices = function(variables, target) {
    const ans = [];
    for (let i = 0; i < variables.length; i++) {
        const v = variables[i];
        const a = v[0], b = v[1], c = v[2], m = v[3];
        if (modPow(modPow(a, b, 10), c, m) === target) ans.push(i);
    }
    return ans;
};
