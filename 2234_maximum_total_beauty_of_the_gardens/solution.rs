// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

impl Solution {
    pub fn maximum_beauty(mut flowers: Vec<i32>, new_flowers: i64, target: i32, full: i32, partial: i32) -> i64 {
        let n = flowers.len();
        for f in flowers.iter_mut() {
            if *f > target {
                *f = target;
            }
        }
        flowers.sort_unstable();
        let sum: i64 = flowers.iter().map(|&f| f as i64).sum();
        if target as i64 * n as i64 - sum <= new_flowers {
            return n as i64 * full as i64;
        }
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + flowers[i] as i64;
        }
        let mut ans = 0i64;
        let mut j = n as i32 - 1;
        let mut remain = new_flowers;
        for complete in 0..=n {
            if complete > 0 {
                let need = target as i64 - flowers[n - complete] as i64;
                if remain < need {
                    break;
                }
                remain -= need;
            }
            while j >= n as i32 - complete as i32
                || (j >= 0 && flowers[j as usize] as i64 * (j as i64 + 1) - pref[j as usize + 1] > remain)
            {
                j -= 1;
            }
            let mut partial_val = 0i64;
            if j >= 0 {
                let extra = (remain - (flowers[j as usize] as i64 * (j as i64 + 1) - pref[j as usize + 1]))
                    / (j as i64 + 1);
                partial_val = flowers[j as usize] as i64 + extra;
                if partial_val >= target as i64 {
                    partial_val = target as i64 - 1;
                }
            }
            ans = ans.max(complete as i64 * full as i64 + partial_val * partial as i64);
        }
        ans
    }
}
