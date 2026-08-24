// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

impl Solution {
    pub fn max_balanced_subsequence_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut keys: Vec<i32> = (0..n).map(|i| nums[i] - i as i32).collect();
        let mut uniq = keys.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let idx_of = |v: i32, uniq: &[i32]| -> usize {
            uniq.binary_search(&v).unwrap_or_else(|e| e) + 1
        };
        const NEG_INF: i64 = -(1i64 << 60);
        let mut bit = vec![NEG_INF; uniq.len() + 2];
        let update = |bit: &mut [i64], mut i: usize, val: i64| {
            while i < bit.len() {
                if val > bit[i] {
                    bit[i] = val;
                }
                i += i & i.wrapping_neg();
            }
        };
        let query = |bit: &[i64], mut i: usize| -> i64 {
            let mut best = NEG_INF;
            while i > 0 {
                if bit[i] > best {
                    best = bit[i];
                }
                i -= i & i.wrapping_neg();
            }
            best
        };
        let mut ans = NEG_INF;
        for i in 0..n {
            let id = idx_of(keys[i], &uniq);
            let best = query(&bit, id);
            let mut cur = nums[i] as i64;
            if best > NEG_INF / 2 {
                cur = cur.max(best + nums[i] as i64);
            }
            update(&mut bit, id, cur);
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
