// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a.abs()
}

impl Solution {
    pub fn min_stable(nums: Vec<i32>, max_c: i32) -> i32 {
        let n = nums.len();
        let ok = |x: usize| -> bool {
            if x >= n {
                return true;
            }
            let mut changes = 0;
            let mut i = 0;
            while i + x < n {
                let mut g = nums[i];
                for j in i + 1..=i + x {
                    g = gcd(g, nums[j]);
                }
                if g > 1 {
                    changes += 1;
                    i += x + 1;
                } else {
                    i += 1;
                }
            }
            changes <= max_c
        };
        let mut lo = 0;
        let mut hi = n;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
