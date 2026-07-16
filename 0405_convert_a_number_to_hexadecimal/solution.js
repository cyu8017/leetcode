// LeetCode 0405 - Convert a Number to Hexadecimal
var toHex = function (num) {
    if (num === 0) return "0";
    const digits = "0123456789abcdef";
    let value = num >>> 0;
    let result = "";
    while (value) {
        result = digits[value & 15] + result;
        value >>>= 4;
    }
    return result;
};

module.exports = { toHex };
