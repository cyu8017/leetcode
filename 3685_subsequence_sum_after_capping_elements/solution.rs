// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

impl Solution {
    pub fn subsequence_sum_after_capping(nums: Vec<i32>, k: i32) -> Vec<bool> {
        let n = nums.len();
        let k = k as usize;
        let mut sorted = nums;
        sorted.sort_unstable();
        let mut ans = vec![false; n];
        let mut reach = vec![false; k + 1];
        reach[0] = true;
        let mut idx = 0;
        for x in 1..=n {
            while idx < n && sorted[idx] as usize <= x {
                let v = sorted[idx] as usize;
                for s in (v..=k).rev() {
                    if reach[s - v] {
                        reach[s] = true;
                    }
                }
                idx += 1;
            }
            let mut tmp = reach.clone();
            let rem = n - idx;
            for s in 0..=k {
                if !reach[s] {
                    continue;
                }
                let mut t = 1;
                while t <= rem && s + t * x <= k {
                    tmp[s + t * x] = true;
                    t += 1;
                }
            }
            ans[x - 1] = tmp[k];
        }
        ans
    }
}
