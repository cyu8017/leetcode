struct Solution;
// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

use std::collections::BTreeMap;

fn merge(st: &mut BTreeMap<i32, i32>, x: i32, v: i32) {
    let c = *st.get(&x).unwrap_or(&0);
    if c + v == 0 {
        st.remove(&x);
    } else {
        st.insert(x, c + v);
    }
}

impl Solution {
    pub fn power_update(nums: Vec<i32>, mut p: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut left: BTreeMap<i32, i32> = BTreeMap::new();
        let mut right: BTreeMap<i32, i32> = BTreeMap::new();
        let mut sz1 = 0i32;
        let mut sz2 = nums.len() as i32;
        for &x in &nums {
            merge(&mut right, x, 1);
        }
        const MOD: i64 = 1_000_000_007;
        let qpow = |mut a: i64, mut b: i32| -> i32 {
            let mut ans = 1i64;
            while b > 0 {
                if b & 1 == 1 {
                    ans = ans * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            ans as i32
        };
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let val = q[0];
            let k = q[1];
            merge(&mut right, val, 1);
            sz2 += 1;
            let node = *right.keys().next().unwrap();
            merge(&mut right, node, -1);
            sz2 -= 1;
            merge(&mut left, node, 1);
            sz1 += 1;
            while sz2 < k {
                let node = *left.keys().next_back().unwrap();
                merge(&mut left, node, -1);
                sz1 -= 1;
                merge(&mut right, node, 1);
                sz2 += 1;
            }
            while sz2 > k {
                let node = *right.keys().next().unwrap();
                merge(&mut right, node, -1);
                sz2 -= 1;
                merge(&mut left, node, 1);
                sz1 += 1;
            }
            let x = *right.keys().next().unwrap();
            p = qpow(p as i64, x);
            ans.push(p);
        }
        let _ = sz1;
        ans
    }
}

fn main() {}
