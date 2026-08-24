// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

impl Solution {
    pub fn max_digit_range(nums: Vec<i32>) -> i32 {
        let mut mx = 0;
        let mut ans = 0;
        for &x in &nums {
            let mut a = 10;
            let mut b = 0;
            let mut y = x;
            while y > 0 {
                let v = y % 10;
                a = a.min(v);
                b = b.max(v);
                y /= 10;
            }
            let r = b - a;
            if mx < r {
                mx = r;
                ans = x;
            } else if mx == r {
                ans += x;
            }
        }
        ans
    }
}
