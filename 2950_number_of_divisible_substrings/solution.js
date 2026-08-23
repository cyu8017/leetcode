// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

var countDivisibleSubstrings = function(word) {
    const vals = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9];
    let ans = 0;
    const n = word.length;
    for (let i = 0; i < n; i++) {
        let sum = 0;
        for (let j = i; j < n; j++) {
            sum += vals[word.charCodeAt(j) - 97];
            if (sum % (j - i + 1) === 0) ans++;
        }
    }
    return ans;
};
