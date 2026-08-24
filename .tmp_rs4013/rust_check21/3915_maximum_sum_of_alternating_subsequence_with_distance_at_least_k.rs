struct Solution;
// LeetCode 3915 - Maximum Sum of Alternating Subsequence With Distance at Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

struct Fenwick {
    f: Vec<i64>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Self { f: vec![0; n] }
    }
    fn update(&mut self, mut i: usize, val: i64) {
        while i < self.f.len() {
            self.f[i] = self.f[i].max(val);
            i += i & i.wrapping_neg();
        }
    }
    fn pre_max(&self, mut i: usize) -> i64 {
        let mut res = 0i64;
        while i > 0 {
            res = res.max(self.f[i]);
            i &= i - 1;
        }
        res
    }
}

impl Solution {
    pub fn max_alternating_sum(mut nums: Vec<i32>, k: i32) -> i64 {
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        sorted.dedup();
        let n = nums.len();
        let m = sorted.len();
        let mut f_inc = vec![0i64; n];
        let mut f_dec = vec![0i64; n];
        let mut inc = Fenwick::new(m + 1);
        let mut dec = Fenwick::new(m + 1);
        let mut ans = 0i64;
        let k = k as usize;
        for i in 0..n {
            let x = nums[i];
            if i >= k {
                let j = nums[i - k];
                inc.update(m - j as usize, f_inc[i - k]);
                dec.update(j as usize + 1, f_dec[i - k]);
            }
            let j = sorted.partition_point(|&v| v < x);
            nums[i] = j as i32;
            f_inc[i] = dec.pre_max(j) + x as i64;
            f_dec[i] = inc.pre_max(m - 1 - j) + x as i64;
            ans = ans.max(f_inc[i]).max(f_dec[i]);
        }
        ans
    }
}
