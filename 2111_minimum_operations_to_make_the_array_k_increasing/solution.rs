// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

impl Solution {
    pub fn k_increasing(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let k = k as usize;
        let mut ans = 0;
        for start in 0..k {
            let seq: Vec<i32> = (start..n).step_by(k).map(|i| arr[i]).collect();
            let mut tails = Vec::new();
            for &x in &seq {
                let i = tails.partition_point(|&t| t <= x);
                if i == tails.len() {
                    tails.push(x);
                } else {
                    tails[i] = x;
                }
            }
            ans += seq.len() as i32 - tails.len() as i32;
        }
        ans
    }
}
