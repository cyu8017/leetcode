// LeetCode 0371 - Sum of Two Integers
var getSum = function(a, b) {
    const mask = 0xffffffff;
    while (b !== 0) {
        const carry = (a & b) << 1;
        a = (a ^ b) & mask;
        b = carry & mask;
    }
    return a >= 0x80000000 ? ~(a ^ mask) : a;
};
