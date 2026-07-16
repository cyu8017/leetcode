// LeetCode 0414 - Third Maximum Number
var thirdMax = function (nums) {
    let first = null;
    let second = null;
    let third = null;
    for (const value of nums) {
        if (value === first || value === second || value === third) continue;
        if (first === null || value > first) {
            third = second;
            second = first;
            first = value;
        } else if (second === null || value > second) {
            third = second;
            second = value;
        } else if (third === null || value > third) {
            third = value;
        }
    }
    return third !== null ? third : first;
};

module.exports = { thirdMax };
