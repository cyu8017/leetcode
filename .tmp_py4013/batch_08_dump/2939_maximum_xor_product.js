// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

var maximumXorProduct = function(a, b, n) {
    const mod = 1000000007n;
    let A = BigInt(a), B = BigInt(b);
    for (let i = n - 1; i >= 0; i--) {
        const bit = 1n << BigInt(i);
        const abit = A & bit, bbit = B & bit;
        if (abit === bbit) {
            A |= bit;
            B |= bit;
        } else if (A > B) {
            B |= bit;
            A &= ~bit;
        } else {
            A |= bit;
            B &= ~bit;
        }
    }
    return Number((A % mod) * (B % mod) % mod);
};
