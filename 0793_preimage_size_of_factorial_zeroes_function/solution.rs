// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

impl Solution {
    pub fn preimage_size_fzf(k: i32) -> i32 {
        let k = k as i64;
        if Self::zeros(Self::first_ge(k)) == k {
            5
        } else {
            0
        }
    }

    fn zeros(mut x: i64) -> i64 {
        let mut count = 0;
        while x > 0 {
            x /= 5;
            count += x;
        }
        count
    }

    fn first_ge(target: i64) -> i64 {
        let mut lo = 0i64;
        let mut hi = 5 * (target + 1);
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if Self::zeros(mid) < target {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        lo
    }
}
