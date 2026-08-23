// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

var getLeastFrequentDigit = function(n) {
    const cnt = new Array(10).fill(0);
    let ans = 0, f = 1 << 30;
    for (; n > 0; n = Math.floor(n / 10)) cnt[n % 10]++;
    for (let x = 0; x < 10; x++) {
        if (cnt[x] > 0 && cnt[x] < f) {
            f = cnt[x];
            ans = x;
        }
    }
    return ans;
};
