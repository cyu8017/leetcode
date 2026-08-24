struct Solution;
// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i64 {
        let k = k as usize;
        let mut even_freq = vec![0i64; k];
        let mut odd_freq = vec![0i64; k];
        for (i, &num) in nums.iter().enumerate() {
            if i % 2 == 0 {
                even_freq[(num as usize) % k] += 1;
            } else {
                odd_freq[(num as usize) % k] += 1;
            }
        }
        let costs = |freq: &[i64]| -> Vec<i64> {
            let mut dbl = vec![0i64; 2 * k];
            for i in 0..(2 * k) {
                dbl[i] = freq[i % k];
            }
            let mut count_prefix = vec![0i64; 2 * k + 1];
            let mut weighted_prefix = vec![0i64; 2 * k + 1];
            for i in 0..(2 * k) {
                count_prefix[i + 1] = count_prefix[i] + dbl[i];
                weighted_prefix[i + 1] = weighted_prefix[i] + i as i64 * dbl[i];
            }
            let range_stats = |l: usize, r: usize| -> (i64, i64) {
                (
                    count_prefix[r + 1] - count_prefix[l],
                    weighted_prefix[r + 1] - weighted_prefix[l],
                )
            };
            let mut res = vec![0i64; k];
            let cw = k / 2;
            let cc = (k - 1) / 2;
            for t in 0..k {
                let (cnt, sum) = range_stats(t, t + cw);
                res[t] += sum - t as i64 * cnt;
                if cc > 0 {
                    let (cnt2, sum2) = range_stats(t + k - cc, t + k - 1);
                    res[t] += (t + k) as i64 * cnt2 - sum2;
                }
            }
            res
        };
        let even_cost = costs(&even_freq);
        let odd_cost = costs(&odd_freq);
        let mut best1 = 1i64 << 62;
        let mut best2 = 1i64 << 62;
        let mut best_index = -1i32;
        for i in 0..k {
            let x = odd_cost[i];
            if x < best1 {
                best2 = best1;
                best1 = x;
                best_index = i as i32;
            } else if x < best2 {
                best2 = x;
            }
        }
        let mut ans = 1i64 << 62;
        for x in 0..k {
            let other = if x as i32 == best_index { best2 } else { best1 };
            ans = ans.min(even_cost[x] + other);
        }
        ans
    }
}

fn main() {}
