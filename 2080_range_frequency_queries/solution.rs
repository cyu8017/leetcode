// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

use std::collections::HashMap;

pub struct RangeFreqQuery {
    pos: HashMap<i32, Vec<i32>>,
}

impl RangeFreqQuery {
    pub fn new(arr: Vec<i32>) -> Self {
        let mut pos = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            pos.entry(v).or_insert_with(Vec::new).push(i as i32);
        }
        Self { pos }
    }

    pub fn query(&self, left: i32, right: i32, value: i32) -> i32 {
        let Some(p) = self.pos.get(&value) else {
            return 0;
        };
        let l = p.partition_point(|&x| x < left);
        let r = p.partition_point(|&x| x <= right);
        (r - l) as i32
    }
}
