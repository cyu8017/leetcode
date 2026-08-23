// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

function check3606(s) {
    if (!s) return false;
    for (const c of s)
        if (!/[A-Za-z0-9_]/.test(c)) return false;
    return true;
}
var validateCoupons = function(code, businessLine, isActive) {
    const bs = new Set(['electronics', 'grocery', 'pharmacy', 'restaurant']);
    const idx = [];
    for (let i = 0; i < code.length; i++) {
        if (isActive[i] && bs.has(businessLine[i]) && check3606(code[i])) idx.push(i);
    }
    idx.sort((i, j) => {
        const c = businessLine[i] < businessLine[j] ? -1 : businessLine[i] > businessLine[j] ? 1 : 0;
        if (c !== 0) return c;
        return code[i] < code[j] ? -1 : code[i] > code[j] ? 1 : 0;
    });
    return idx.map(i => code[i]);
};
