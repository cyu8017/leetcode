// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

use std::collections::BTreeSet;

impl Solution {
    pub fn min_operations(s: String, k: i32) -> i32 {
        let n = s.len() as i32;
        let mut ts = [BTreeSet::new(), BTreeSet::new()];
        for i in 0..=n {
            ts[(i % 2) as usize].insert(i);
        }
        let cnt0 = s.bytes().filter(|&c| c == b'0').count() as i32;
        ts[(cnt0 % 2) as usize].remove(&cnt0);
        let mut q = vec![cnt0];
        let mut ans = 0;
        while !q.is_empty() {
            let mut nq = Vec::new();
            for cur in q {
                if cur == 0 {
                    return ans;
                }
                let l = cur + k - 2 * cur.min(k);
                let r = cur + k - 2 * (k - n + cur).max(0);
                let t = &mut ts[(l % 2) as usize];
                let mut to_erase = Vec::new();
                for &v in t.range(l..=r) {
                    nq.push(v);
                    to_erase.push(v);
                }
                for v in to_erase {
                    t.remove(&v);
                }
            }
            q = nq;
            ans += 1;
        }
        -1
    }
}
