// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    fn mod_pow(mut a: i64, mut e: i64, m: i64) -> i64 {
        let mut r = 1;
        a %= m;
        while e > 0 {
            if e & 1 == 1 {
                r = r * a % m;
            }
            a = a * a % m;
            e >>= 1;
        }
        r
    }

    pub fn get_final_state(mut nums: Vec<i32>, mut k: i32, multiplier: i32) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        if multiplier == 1 {
            return nums;
        }
        let mut h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut max_v = 0;
        for (i, &v) in nums.iter().enumerate() {
            h.push(Reverse((v, i)));
            if v > max_v {
                max_v = v;
            }
        }
        while k > 0 && !h.is_empty() {
            let Reverse((v, i)) = h.pop().unwrap();
            if v as i64 * multiplier as i64 > max_v as i64 && k >= nums.len() as i32 {
                h.push(Reverse((v, i)));
                break;
            }
            let nv = v * multiplier;
            nums[i] = nv;
            if nv > max_v {
                max_v = nv;
            }
            h.push(Reverse((nv, i)));
            k -= 1;
        }
        if k > 0 {
            let n = nums.len() as i32;
            let full = k / n;
            let rem = k % n;
            let pow_full = Self::mod_pow(multiplier as i64, full as i64, MOD);
            for x in &mut nums {
                *x = ((*x as i64) * pow_full % MOD) as i32;
            }
            let mut hh: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
            for (i, &v) in nums.iter().enumerate() {
                hh.push(Reverse((v, i)));
            }
            for _ in 0..rem {
                let Reverse((v, i)) = hh.pop().unwrap();
                let nv = ((v as i64) * multiplier as i64 % MOD) as i32;
                nums[i] = nv;
                hh.push(Reverse((nv, i)));
            }
            for x in &mut nums {
                *x %= MOD as i32;
            }
        } else {
            for x in &mut nums {
                *x %= MOD as i32;
            }
        }
        nums
    }
}
