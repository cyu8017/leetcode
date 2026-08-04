// LeetCode 1413: Minimum Value To Get Positive Step By Step Sum

var minStartValue = function(nums) {
    let sum = 0, minimum = 0;
    for (const value of nums) { sum += value; minimum = Math.min(minimum, sum); }
    return 1 - minimum;
};
