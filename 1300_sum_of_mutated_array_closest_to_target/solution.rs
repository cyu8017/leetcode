// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

impl Solution {
    pub fn find_best_value(arr: Vec<i32>, target: i32) -> i32 {
        let mut lo = 0;
        let mut hi = *arr.iter().max().unwrap_or(&0);
        let sum_at = |v: i32| -> i32 { arr.iter().map(|&x| x.min(v)).sum() };
        while lo < hi {
            let mid = (lo + hi) / 2;
            if sum_at(mid) < target {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        let before = sum_at(lo - 1);
        let after = sum_at(lo);
        if target - before <= after - target { lo - 1 } else { lo }
    }
}
