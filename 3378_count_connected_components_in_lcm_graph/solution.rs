// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

use std::collections::{HashMap, HashSet};

impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    pub fn count_components(nums: Vec<i32>, threshold: i32) -> i32 {
        let n = nums.len();
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(x: usize, parent: &mut [usize]) -> usize {
            if parent[x] != x {
                parent[x] = find(parent[x], parent);
            }
            parent[x]
        }
        let unite = |a: usize, b: usize, parent: &mut [usize]| {
            let ra = find(a, parent);
            let rb = find(b, parent);
            if ra != rb {
                parent[ra] = rb;
            }
        };
        let mut idx = HashMap::new();
        for i in 0..n {
            idx.insert(nums[i], i);
        }
        for d in 1..=threshold {
            let mut first = None;
            let mut m = d;
            while m <= threshold {
                if let Some(&i) = idx.get(&m) {
                    match first {
                        None => first = Some(i),
                        Some(f) => {
                            if nums[f] as i64 * nums[i] as i64 / Self::gcd(nums[f], nums[i]) as i64
                                <= threshold as i64
                            {
                                unite(f, i, &mut parent);
                            }
                        }
                    }
                }
                m += d;
            }
        }
        for i in 0..n {
            for j in i + 1..n {
                let a = nums[i];
                let b = nums[j];
                let g = Self::gcd(a, b);
                if a as i64 / g as i64 * b as i64 <= threshold as i64 {
                    unite(i, j, &mut parent);
                }
            }
        }
        let mut comp = HashSet::new();
        for i in 0..n {
            comp.insert(find(i, &mut parent));
        }
        comp.len() as i32
    }
}
