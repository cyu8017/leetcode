// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

use std::collections::BTreeSet;

impl Solution {
    pub fn brace_expansion_ii(expression: String) -> Vec<String> {
        let (result, _) = Self::parse(expression.as_bytes(), 0);
        result.into_iter().collect()
    }

    fn parse(expr: &[u8], mut i: usize) -> (BTreeSet<String>, usize) {
        let mut union_set: BTreeSet<String> = BTreeSet::new();
        let mut cur: BTreeSet<String> = BTreeSet::from([String::new()]);
        while i < expr.len() && expr[i] != b'}' {
            if expr[i] == b'{' {
                let (nested, ni) = Self::parse(expr, i + 1);
                i = ni;
                let mut next = BTreeSet::new();
                for a in &cur {
                    for b in &nested {
                        next.insert(format!("{}{}", a, b));
                    }
                }
                cur = next;
            } else if expr[i] == b',' {
                union_set.extend(cur);
                cur = BTreeSet::from([String::new()]);
                i += 1;
            } else {
                let mut j = i;
                while j < expr.len() && expr[j].is_ascii_alphabetic() {
                    j += 1;
                }
                let token = String::from_utf8(expr[i..j].to_vec()).unwrap();
                let mut next = BTreeSet::new();
                for a in &cur {
                    next.insert(format!("{}{}", a, token));
                }
                cur = next;
                i = j;
            }
        }
        union_set.extend(cur);
        (union_set, i + 1)
    }
}
