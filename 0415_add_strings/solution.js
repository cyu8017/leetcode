// LeetCode 0415 - Add Strings
var addStrings = function (num1, num2) {
    let index1 = num1.length - 1;
    let index2 = num2.length - 1;
    let carry = 0;
    const digits = [];
    while (index1 >= 0 || index2 >= 0 || carry) {
        if (index1 >= 0) carry += Number(num1[index1--]);
        if (index2 >= 0) carry += Number(num2[index2--]);
        digits.push(String(carry % 10));
        carry = Math.floor(carry / 10);
    }
    return digits.reverse().join("");
};

module.exports = { addStrings };
