// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

use std::collections::HashMap;

impl Solution {
    pub fn popcount_depth(n: i64, k: i32) -> i64 {
        if k == 0 {
            return if n >= 1 { 1 } else { 0 };
        }
        fn depth(mut x: i32) -> i32 {
            if x <= 0 {
                return 100;
            }
            let mut d = 0;
            while x > 1 {
                x = x.count_ones() as i32;
                d += 1;
            }
            d
        }
        let mut bits = Vec::new();
        let mut x = n;
        while x > 0 {
            bits.push((x & 1) as u8);
            x >>= 1;
        }
        bits.reverse();
        if bits.is_empty() {
            bits.push(0);
        }
        let mut memo: HashMap<(i32, i32, i32, i32), i64> = HashMap::new();
        fn dfs(
            pos: i32,
            tight: i32,
            started: i32,
            pc: i32,
            bits: &[u8],
            k: i32,
            memo: &mut HashMap<(i32, i32, i32, i32), i64>,
        ) -> i64 {
            if pos == bits.len() as i32 {
                if started == 0 {
                    return 0;
                }
                if pc == 1 {
                    return if k == 1 { 1 } else { 0 };
                }
                return if depth(pc) == k - 1 { 1 } else { 0 };
            }
            let key = (pos, tight, started, pc);
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            let up = if tight == 1 { bits[pos as usize] as i32 } else { 1 };
            let mut res = 0i64;
            for dig in 0..=up {
                let nt = if tight == 1 && dig == up { 1 } else { 0 };
                if started == 0 && dig == 0 {
                    res += dfs(pos + 1, nt, 0, 0, bits, k, memo);
                } else {
                    res += dfs(pos + 1, nt, 1, pc + dig, bits, k, memo);
                }
            }
            memo.insert(key, res);
            res
        }
        dfs(0, 1, 0, 0, &bits, k, &mut memo)
    }
}
