// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

var countDigitOccurrences = function(nums, digit) {
    let ans = 0;
    for (let num of nums) {
        let x = num;
        for (; x > 0; x = Math.floor(x / 10)) {
            if (x % 10 === digit) ans++;
        }
    }
    return ans;
};
