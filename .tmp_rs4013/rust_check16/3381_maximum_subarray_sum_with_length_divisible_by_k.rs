struct Solution;
// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        const INF: i64 = 1i64 << 62;
        let mut best = vec![INF; k];
        best[0] = 0;
        let mut ans = -(1i64 << 62);
        for i in 1..=n {
            let r = i % k;
            if best[r] != INF {
                let cand = pref[i] - best[r];
                if cand > ans {
                    ans = cand;
                }
            }
            if pref[i] < best[r] {
                best[r] = pref[i];
            }
        }
        ans
    }
}

fn main() {}
