// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

use std::collections::{HashMap, HashSet};

struct MajorityChecker {
    arr: Vec<i32>,
    pos: HashMap<i32, Vec<usize>>,
}

impl MajorityChecker {
    fn new(arr: Vec<i32>) -> Self {
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            pos.entry(v).or_default().push(i);
        }
        Self { arr, pos }
    }

    fn query(&self, left: i32, right: i32, threshold: i32) -> i32 {
        let left = left as usize;
        let right = right as usize;
        let span = right - left + 1;
        let mut seen = HashSet::new();
        let trials = 30.min(span);
        for t in 0..trials {
            let cand = self.arr[left + (t * 7919 + 13) % span];
            if !seen.insert(cand) {
                continue;
            }
            let arr = &self.pos[&cand];
            let lo = arr.partition_point(|&x| x < left);
            let hi = arr.partition_point(|&x| x <= right);
            if (hi - lo) as i32 >= threshold {
                return cand;
            }
        }
        -1
    }
}
