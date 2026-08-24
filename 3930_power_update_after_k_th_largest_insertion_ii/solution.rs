// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

impl Solution {
    pub fn power_update(nums: Vec<i32>, p: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        let mut vals = nums.clone();
        for q in &queries {
            vals.push(q[0]);
        }
        vals.sort_unstable();
        vals.dedup();
        let mut bit = vec![0i32; vals.len() + 1];
        let add = |bit: &mut [i32], mut i: usize| {
            while i < bit.len() {
                bit[i] += 1;
                i += i & i.wrapping_neg();
            }
        };
        let kth = |bit: &[i32], vals: &[i32], mut rank: i32| -> i32 {
            let mut idx = 0usize;
            let mut step = 1usize;
            while (step << 1) < bit.len() {
                step <<= 1;
            }
            while step > 0 {
                let next = idx + step;
                if next < bit.len() && bit[next] < rank {
                    idx = next;
                    rank -= bit[next];
                }
                step >>= 1;
            }
            vals[idx]
        };
        for &x in &nums {
            let pos = vals.binary_search(&x).unwrap_or_else(|e| e) + 1;
            add(&mut bit, pos);
        }
        let powm = |mut a: i64, mut e: i64| -> i64 {
            let mut res = 1i64;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res
        };
        let mut ans = vec![0i32; queries.len()];
        let mut size = nums.len() as i32;
        let mut cur = p as i64;
        for (i, q) in queries.iter().enumerate() {
            let pos = vals.binary_search(&q[0]).unwrap_or_else(|e| e) + 1;
            add(&mut bit, pos);
            size += 1;
            let x = kth(&bit, &vals, size - q[1] + 1);
            cur = powm(cur, x as i64);
            ans[i] = cur as i32;
        }
        ans
    }
}
