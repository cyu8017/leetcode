// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

impl Solution {
    fn count_le(m: i32, n: i32, x: i32) -> i32 {
        let mut count = 0;
        for row in 1..=m {
            count += (x / row).min(n);
        }
        count
    }

    pub fn find_kth_number(m: i32, n: i32, k: i32) -> i32 {
        let mut lo = 1;
        let mut hi = m * n;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if Self::count_le(m, n, mid) >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
