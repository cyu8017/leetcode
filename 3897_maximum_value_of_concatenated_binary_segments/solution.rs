// LeetCode 3897 - Maximum Value of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

impl Solution {
    pub fn max_value(nums1: Vec<i32>, nums0: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn group(p: &(i32, i32)) -> i32 {
            if p.1 == 0 {
                0
            } else if p.0 > 0 {
                1
            } else {
                2
            }
        }
        let n = nums1.len();
        let mut pairs: Vec<(i32, i32)> = (0..n).map(|i| (nums1[i], nums0[i])).collect();
        let mut b: i32 = pairs.iter().map(|(a, c)| a + c).sum();
        pairs.sort_by(|a, b| {
            let g1 = group(a);
            let g2 = group(b);
            if g1 != g2 {
                return g1.cmp(&g2);
            }
            if g1 == 0 {
                return b.0.cmp(&a.0);
            }
            if g1 == 1 {
                if a.0 != b.0 {
                    return b.0.cmp(&a.0);
                }
                return a.1.cmp(&b.1);
            }
            a.1.cmp(&b.1)
        });
        let mut p = vec![0i32; b as usize];
        p[0] = 1;
        for i in 1..b as usize {
            p[i] = (2i64 * p[i - 1] as i64 % MOD) as i32;
        }
        let mut ans = 0i32;
        b -= 1;
        for (mut cnt1, cnt0) in pairs {
            while cnt1 > 0 {
                ans = (ans + p[b as usize]) % MOD as i32;
                b -= 1;
                cnt1 -= 1;
            }
            b -= cnt0;
        }
        ans
    }
}
