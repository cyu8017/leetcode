// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/
var maxDigitRange = function(nums) {
        let mx = 0, ans = 0;
        for (const x of nums) {
            let a = 10, b = 0;
            for (let y = x; y > 0; y /= 10) {
                let v = y % 10;
                a = Math.min(a, v);
                b = Math.max(b, v);
            }
            let r = b - a;
            if (mx < r) {
                mx = r;
                ans = x;
            } else if (mx == r) {
                ans += x;
            }
        }
        return ans;
    
};
