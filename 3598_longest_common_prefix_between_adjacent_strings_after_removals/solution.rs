// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

use std::collections::BTreeMap;

impl Solution {
    pub fn longest_common_prefix(words: Vec<String>) -> Vec<i32> {
        let n = words.len();
        let mut tm: BTreeMap<i32, i32> = BTreeMap::new();
        let calc = |s: &str, t: &str| -> i32 {
            let m = s.len().min(t.len());
            let sb = s.as_bytes();
            let tb = t.as_bytes();
            for k in 0..m {
                if sb[k] != tb[k] {
                    return k as i32;
                }
            }
            m as i32
        };
        let add = |tm: &mut BTreeMap<i32, i32>, words: &[String], i: i32, j: i32| {
            if i >= 0 && (i as usize) < n && j >= 0 && (j as usize) < n {
                *tm.entry(calc(&words[i as usize], &words[j as usize])).or_insert(0) += 1;
            }
        };
        let remove = |tm: &mut BTreeMap<i32, i32>, words: &[String], i: i32, j: i32| {
            if i >= 0 && (i as usize) < n && j >= 0 && (j as usize) < n {
                let x = calc(&words[i as usize], &words[j as usize]);
                if let Some(c) = tm.get_mut(&x) {
                    *c -= 1;
                    if *c == 0 {
                        tm.remove(&x);
                    }
                }
            }
        };
        for i in 0..n.saturating_sub(1) {
            add(&mut tm, &words, i as i32, i as i32 + 1);
        }
        let mut ans = vec![0; n];
        for i in 0..n {
            let i32i = i as i32;
            remove(&mut tm, &words, i32i, i32i + 1);
            remove(&mut tm, &words, i32i - 1, i32i);
            add(&mut tm, &words, i32i - 1, i32i + 1);
            if let Some((&mx, _)) = tm.iter().next_back() {
                if mx > 0 {
                    ans[i] = mx;
                }
            }
            remove(&mut tm, &words, i32i - 1, i32i + 1);
            add(&mut tm, &words, i32i - 1, i32i);
            add(&mut tm, &words, i32i, i32i + 1);
        }
        ans
    }
}
