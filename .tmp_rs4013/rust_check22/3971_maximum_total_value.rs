struct Solution;
// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

impl Solution {
    pub fn maximum_total_value(value: Vec<i32>, decay: Vec<i32>, m: i64) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let count_at_least = |threshold: i64| -> i64 {
            let mut count = 0i64;
            for i in 0..value.len() {
                if value[i] as i64 >= threshold {
                    count += (value[i] as i64 - threshold) / decay[i] as i64 + 1;
                }
            }
            count
        };
        if count_at_least(1) <= m {
            let mut sum = 0i64;
            for i in 0..value.len() {
                let terms = (value[i] as i64 - 1) / decay[i] as i64 + 1;
                sum = (sum + terms * value[i] as i64 - decay[i] as i64 * terms * (terms - 1) / 2) % MOD;
            }
            return sum as i32;
        }
        let mut high = 0i64;
        for &v in &value {
            if v as i64 > high {
                high = v as i64;
            }
        }
        let mut low = 1i64;
        while low < high {
            let mid = (low + high + 1) / 2;
            if count_at_least(mid) >= m {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        let threshold = low;
        let mut count = 0i64;
        let mut sum = 0i64;
        for i in 0..value.len() {
            if (value[i] as i64) < threshold {
                continue;
            }
            let terms = (value[i] as i64 - threshold) / decay[i] as i64 + 1;
            count += terms;
            sum = (sum
                + (terms * value[i] as i64 - decay[i] as i64 * terms * (terms - 1) / 2) % MOD)
                % MOD;
        }
        sum = (sum - ((count - m) % MOD) * (threshold % MOD)) % MOD;
        if sum < 0 {
            sum += MOD;
        }
        sum as i32
    }
}

fn main() {}
