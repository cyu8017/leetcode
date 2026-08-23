// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

/**
 * @param {string} num
 * @return {boolean}
 */
var isAdditiveNumber = function(num) {
    function valid(first, second, start) {
        if ((first.length > 1 && first[0] === "0") || (second.length > 1 && second[0] === "0")) {
            return false;
        }
        while (start < num.length) {
            const total = String(Number(first) + Number(second));
            if (!num.startsWith(total, start)) {
                return false;
            }
            first = second;
            second = total;
            start += total.length;
        }
        return true;
    }

    for (let firstEnd = 1; firstEnd < num.length; firstEnd += 1) {
        for (let secondEnd = firstEnd + 1; secondEnd < num.length; secondEnd += 1) {
            if (valid(num.slice(0, firstEnd), num.slice(firstEnd, secondEnd), secondEnd)) {
                return true;
            }
        }
    }
    return false;
};
