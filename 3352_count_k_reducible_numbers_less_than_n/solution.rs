// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

use std::collections::HashMap;

impl Solution {
    fn bits_pop(mut x: i32) -> i32 {
        let mut c = 0;
        while x > 0 {
            c += x & 1;
            x >>= 1;
        }
        c
    }

    pub fn count_k_reducible_numbers(s: String, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut red = vec![0i32; 801];
        red[1] = 0;
        for i in 2..=800 {
            red[i] = 1 + red[Self::bits_pop(i as i32) as usize];
        }
        let n = s.len();
        let sb = s.as_bytes();
        let mut memo: HashMap<(i32, i32, i32), i32> = HashMap::new();
        fn dfs(
            pos: usize,
            tight: bool,
            ones: i32,
            n: usize,
            sb: &[u8],
            k: i32,
            red: &[i32],
            memo: &mut HashMap<(i32, i32, i32), i32>,
        ) -> i32 {
            if pos == n {
                if ones == 0 {
                    return 0;
                }
                return if red[ones as usize] <= k - 1 { 1 } else { 0 };
            }
            let key = (pos as i32, if tight { 1 } else { 0 }, ones);
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            let up = if tight { (sb[pos] - b'0') as i32 } else { 1 };
            let mut ans = 0;
            for d in 0..=up {
                let nt = tight && d == up;
                ans = (ans + dfs(pos + 1, nt, ones + d, n, sb, k, red, memo)) % 1_000_000_007;
            }
            memo.insert(key, ans);
            ans
        }
        dfs(0, true, 0, n, sb, k, &red, &mut memo)
    }
}
