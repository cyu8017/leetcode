// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i64 {
        let max_v = nums.iter().copied().max().unwrap_or(0);
        let mut bits_n = 0usize;
        let mut x = max_v;
        while x > 0 {
            bits_n += 1;
            x >>= 1;
        }
        if bits_n == 0 {
            bits_n = 1;
        }
        let size = 1usize << bits_n;
        let mut best = vec![0i32; size];
        for &v in &nums {
            if v > best[v as usize] {
                best[v as usize] = v;
            }
        }
        for mask in 0..size {
            for b in 0..bits_n {
                if mask & (1usize << b) != 0 {
                    let sub = mask ^ (1usize << b);
                    if best[sub] > best[mask] {
                        best[mask] = best[sub];
                    }
                }
            }
        }
        let mut ans = 0i64;
        for &v in &nums {
            let comp = (size - 1) ^ v as usize;
            if best[comp] > 0 {
                let p = v as i64 * best[comp] as i64;
                if p > ans {
                    ans = p;
                }
            }
        }
        ans
    }
}
