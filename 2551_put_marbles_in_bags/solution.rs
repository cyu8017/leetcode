// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

impl Solution {
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        let n = weights.len();
        if k == 1 || k as usize == n {
            return 0;
        }
        let mut pair: Vec<i32> = (0..n - 1).map(|i| weights[i] + weights[i + 1]).collect();
        pair.sort_unstable();
        let mut mn = 0i64;
        let mut mx = 0i64;
        for i in 0..(k as usize - 1) {
            mn += pair[i] as i64;
            mx += pair[n - 2 - i] as i64;
        }
        mx - mn
    }
}
