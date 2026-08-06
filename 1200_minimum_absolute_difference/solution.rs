// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

impl Solution {
    pub fn minimum_abs_difference(mut arr: Vec<i32>) -> Vec<Vec<i32>> {
        arr.sort_unstable();
        let mut best = arr[1] - arr[0];
        for i in 2..arr.len() {
            best = best.min(arr[i] - arr[i - 1]);
        }
        let mut ans = Vec::new();
        for i in 1..arr.len() {
            if arr[i] - arr[i - 1] == best {
                ans.push(vec![arr[i - 1], arr[i]]);
            }
        }
        ans
    }
}
