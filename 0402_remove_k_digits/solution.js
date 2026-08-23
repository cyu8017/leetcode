// LeetCode 0402 - Remove K Digits
var removeKdigits = function (num, k) {
    const stack = [];
    for (const digit of num) {
        while (k && stack.length && stack[stack.length - 1] > digit) {
            stack.pop();
            k -= 1;
        }
        stack.push(digit);
    }
    if (k) stack.splice(stack.length - k);
    const result = stack.join("").replace(/^0+/, "");
    return result || "0";
};

module.exports = { removeKdigits };
