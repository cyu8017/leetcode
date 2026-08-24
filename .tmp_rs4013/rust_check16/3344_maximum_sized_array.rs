struct Solution;
// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

impl Solution {
    pub fn max_sized_array(s: i64) -> i32 {
        let ok = |n: i64| -> bool {
            let mut sum = 0i64;
            for i in 0..n {
                for j in 0..n {
                    let ij = i | j;
                    sum += ij * (n - 1) * n / 2;
                    if sum > s {
                        return false;
                    }
                }
            }
            sum <= s
        };
        let mut lo = 1i64;
        let mut hi = 2000i64;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}

fn main() {}
