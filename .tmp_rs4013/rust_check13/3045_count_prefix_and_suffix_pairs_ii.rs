#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

use std::collections::HashMap;

struct Node {
    children: HashMap<i32, usize>,
    cnt: i64,
}

impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i64 {
        let mut nodes = vec![Node {
            children: HashMap::new(),
            cnt: 0,
        }];
        let mut ans = 0i64;
        for s in &words {
            let b = s.as_bytes();
            let m = b.len();
            let mut node = 0usize;
            for i in 0..m {
                let p = b[i] as i32 * 32 + b[m - i - 1] as i32;
                let nxt = if let Some(&id) = nodes[node].children.get(&p) {
                    id
                } else {
                    let id = nodes.len();
                    nodes.push(Node {
                        children: HashMap::new(),
                        cnt: 0,
                    });
                    nodes[node].children.insert(p, id);
                    id
                };
                node = nxt;
                ans += nodes[node].cnt;
            }
            nodes[node].cnt += 1;
        }
        ans
    }
}
