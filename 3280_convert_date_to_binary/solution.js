// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

var convertDateToBinary = function(date) {
    const toBinary = (v) => {
        if (v === 0) return '0';
        let s = '';
        while (v > 0) { s = String(v & 1) + s; v >>= 1; }
        return s;
    };
    const parts = date.split('-');
    const y = parseInt(parts[0], 10), m = parseInt(parts[1], 10), d = parseInt(parts[2], 10);
    return toBinary(y) + '-' + toBinary(m) + '-' + toBinary(d);
};
