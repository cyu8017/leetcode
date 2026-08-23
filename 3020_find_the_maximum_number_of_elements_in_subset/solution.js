// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

var maximumLength = function(nums) {
    const cnt = new Map();
    for (const x of nums) cnt.set(x, (cnt.get(x) || 0) + 1);
    const ones = cnt.get(1) || 0;
    let ans = ones - ((ones % 2) ^ 1);
    cnt.delete(1);
    const keys = [...cnt.keys()];
    for (const start of keys) {
        let x = start;
        let t = 0;
        while ((cnt.get(x) || 0) > 1) {
            x = x * x;
            t += 2;
        }
        if ((cnt.get(x) || 0) > 0) t += 1;
        else t -= 1;
        ans = Math.max(ans, t);
    }
    return ans;
};
