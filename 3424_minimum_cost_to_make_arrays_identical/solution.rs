// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

impl Solution {
    pub fn min_cost(arr: Vec<i32>, brr: Vec<i32>, k: i64) -> i64 {
        let mut no_swap = 0i64;
        for i in 0..arr.len() {
            no_swap += (arr[i] - brr[i]).abs() as i64;
        }
        let mut a2 = arr;
        let mut b2 = brr;
        a2.sort_unstable();
        b2.sort_unstable();
        let mut with_swap = k;
        for i in 0..a2.len() {
            with_swap += (a2[i] - b2[i]).abs() as i64;
        }
        no_swap.min(with_swap)
    }
}
