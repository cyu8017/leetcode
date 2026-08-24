// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

impl Solution {
    pub fn largest_integer(num: i32) -> i32 {
        let mut digits = Vec::new();
        let mut x = num;
        if x == 0 {
            digits.push(0);
        }
        while x > 0 {
            digits.insert(0, x % 10);
            x /= 10;
        }
        let mut even: Vec<i32> = digits.iter().copied().filter(|d| d % 2 == 0).collect();
        let mut odd: Vec<i32> = digits.iter().copied().filter(|d| d % 2 != 0).collect();
        even.sort_unstable_by(|a, b| b.cmp(a));
        odd.sort_unstable_by(|a, b| b.cmp(a));
        let mut ei = 0;
        let mut oi = 0;
        let mut ans = 0;
        for d in digits {
            if d % 2 == 0 {
                ans = ans * 10 + even[ei];
                ei += 1;
            } else {
                ans = ans * 10 + odd[oi];
                oi += 1;
            }
        }
        ans
    }
}
