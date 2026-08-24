// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

use std::collections::HashMap;

impl Solution {
    pub fn largest_component_size(nums: Vec<i32>) -> i32 {
        let mx = *nums.iter().max().unwrap() as usize;
        let mut parent: Vec<usize> = (0..=mx).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        fn factors(mut x: i32) -> Vec<i32> {
            let mut res = Vec::new();
            let mut d = 2;
            while d * d <= x {
                if x % d == 0 {
                    res.push(d);
                    while x % d == 0 {
                        x /= d;
                    }
                }
                d += 1;
            }
            if x > 1 {
                res.push(x);
            }
            res
        }
        for &num in &nums {
            for f in factors(num) {
                let a = find(&mut parent, num as usize);
                let b = find(&mut parent, f as usize);
                parent[a] = b;
            }
        }
        let mut cnt = HashMap::new();
        let mut ans = 0;
        for &num in &nums {
            let r = find(&mut parent, num as usize);
            let e = cnt.entry(r).or_insert(0);
            *e += 1;
            ans = ans.max(*e);
        }
        ans
    }
}
