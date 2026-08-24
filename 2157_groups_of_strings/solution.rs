// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

use std::collections::{HashMap, HashSet};

impl Solution {
    fn find(parent: &mut HashMap<i32, i32>, x: i32) -> i32 {
        let p = parent[&x];
        if p != x {
            let r = Self::find(parent, p);
            parent.insert(x, r);
        }
        parent[&x]
    }

    fn unite(parent: &mut HashMap<i32, i32>, size: &mut HashMap<i32, i32>, a: i32, b: i32) {
        let mut ra = Self::find(parent, a);
        let mut rb = Self::find(parent, b);
        if ra == rb {
            return;
        }
        if size[&ra] < size[&rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        parent.insert(rb, ra);
        *size.get_mut(&ra).unwrap() += size[&rb];
    }

    fn mask_of(w: &str) -> i32 {
        let mut m = 0;
        for c in w.bytes() {
            m |= 1 << (c - b'a');
        }
        m
    }

    pub fn group_strings(words: Vec<String>) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for w in &words {
            *freq.entry(Self::mask_of(w)).or_insert(0) += 1;
        }
        let mut parent = HashMap::new();
        let mut size = HashMap::new();
        for (&m, &c) in &freq {
            parent.insert(m, m);
            size.insert(m, c);
        }
        let keys: Vec<i32> = freq.keys().copied().collect();
        for &m in &keys {
            for b in 0..26 {
                if m & (1 << b) != 0 {
                    let nm = m ^ (1 << b);
                    if freq.contains_key(&nm) {
                        Self::unite(&mut parent, &mut size, m, nm);
                    }
                    for a in 0..26 {
                        if (nm & (1 << a)) == 0 {
                            let rm = nm | (1 << a);
                            if freq.contains_key(&rm) {
                                Self::unite(&mut parent, &mut size, m, rm);
                            }
                        }
                    }
                } else {
                    let nm = m | (1 << b);
                    if freq.contains_key(&nm) {
                        Self::unite(&mut parent, &mut size, m, nm);
                    }
                }
            }
        }
        let mut groups = 0;
        let mut max_size = 0;
        let mut seen = HashSet::new();
        for &m in &keys {
            let r = Self::find(&mut parent, m);
            if seen.insert(r) {
                groups += 1;
                max_size = max_size.max(size[&r]);
            }
        }
        vec![groups, max_size]
    }
}
