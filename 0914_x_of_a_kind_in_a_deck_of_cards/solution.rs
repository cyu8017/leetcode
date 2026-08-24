// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

use std::collections::HashMap;

impl Solution {
    pub fn has_groups_size_x(deck: Vec<i32>) -> bool {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let mut count = HashMap::new();
        for x in deck {
            *count.entry(x).or_insert(0) += 1;
        }
        let mut g = 0;
        for c in count.values() {
            g = gcd(g, *c);
        }
        g >= 2
    }
}
