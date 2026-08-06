// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

use std::collections::HashMap;

impl Solution {
    pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
        let n = s.len();
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        for p in pairs {
            let a = find(&mut parent, p[0] as usize);
            let b = find(&mut parent, p[1] as usize);
            parent[a] = b;
        }
        let bytes = s.as_bytes();
        let mut groups: HashMap<usize, Vec<u8>> = HashMap::new();
        for i in 0..n {
            let r = find(&mut parent, i);
            groups.entry(r).or_default().push(bytes[i]);
        }
        for g in groups.values_mut() {
            g.sort_unstable_by(|a, b| b.cmp(a));
        }
        let mut out = vec![0u8; n];
        for i in 0..n {
            let r = find(&mut parent, i);
            let g = groups.get_mut(&r).unwrap();
            out[i] = g.pop().unwrap();
        }
        String::from_utf8(out).unwrap()
    }
}
