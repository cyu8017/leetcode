// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

impl Solution {
    pub fn min_inversion_count(nums: Vec<i32>, k: i32) -> i64 {
        let mut vals = nums.clone();
        vals.sort_unstable();
        vals.dedup();
        let mut bit = vec![0i32; vals.len() + 1];
        let add = |bit: &mut [i32], mut i: usize, delta: i32| {
            while i < bit.len() {
                bit[i] += delta;
                i += i & i.wrapping_neg();
            }
        };
        let sum = |bit: &[i32], mut i: usize| {
            let mut res = 0;
            while i > 0 {
                res += bit[i];
                i -= i & i.wrapping_neg();
            }
            res
        };
        let mut rank = vec![0usize; nums.len()];
        let mut inv = 0i64;
        let k = k as usize;
        for i in 0..nums.len() {
            rank[i] = vals.partition_point(|&v| v < nums[i]) + 1;
            if i < k {
                inv += i as i64 - sum(&bit, rank[i]) as i64;
                add(&mut bit, rank[i], 1);
            }
        }
        let mut best = inv;
        for r in k..nums.len() {
            let left = rank[r - k];
            inv -= sum(&bit, left - 1) as i64;
            add(&mut bit, left, -1);
            inv += (k as i64 - 1) - sum(&bit, rank[r]) as i64;
            add(&mut bit, rank[r], 1);
            if inv < best {
                best = inv;
            }
        }
        best
    }
}
