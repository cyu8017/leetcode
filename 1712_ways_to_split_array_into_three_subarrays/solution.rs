// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

impl Solution {
    pub fn ways_to_split(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut prefix = vec![0i64; n];
        let mut total = 0i64;
        for (i, &v) in nums.iter().enumerate() {
            total += v as i64;
            prefix[i] = total;
        }

        let lower_bound = |target: i64, mut lo: usize, mut hi: usize| -> usize {
            while lo < hi {
                let mid = (lo + hi) / 2;
                if prefix[mid] < target {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            lo
        };

        let upper_bound = |target: i64, mut lo: usize, mut hi: usize| -> usize {
            while lo < hi {
                let mid = (lo + hi) / 2;
                if prefix[mid] <= target {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            lo
        };

        let mut ans = 0i64;
        for i in 0..n - 2 {
            let left = prefix[i];
            let lo = lower_bound(2 * left, i + 1, n - 1);
            let hi = upper_bound((total + left) / 2, lo, n - 1);
            ans = (ans + (hi - lo) as i64) % MOD;
        }
        ans as i32
    }
}
