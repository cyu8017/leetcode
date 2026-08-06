// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_smallest_region(
        regions: Vec<Vec<String>>,
        mut region1: String,
        mut region2: String,
    ) -> String {
        let mut parent = HashMap::new();
        for group in regions {
            for child in &group[1..] {
                parent.insert(child.clone(), group[0].clone());
            }
        }
        let mut ancestors = HashSet::new();
        loop {
            ancestors.insert(region1.clone());
            match parent.get(&region1) {
                Some(p) => region1 = p.clone(),
                None => break,
            }
        }
        while !ancestors.contains(&region2) {
            region2 = parent[&region2].clone();
        }
        region2
    }
}
