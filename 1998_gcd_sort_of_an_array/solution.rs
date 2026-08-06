// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

use std::collections::HashSet;

impl Solution {
    pub fn gcd_sort(nums: Vec<i32>) -> bool {
        let m = *nums.iter().max().unwrap() as usize;
        let mut parent: Vec<usize> = (0..=m).collect();

        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }

        fn union(parent: &mut [usize], a: usize, b: usize) {
            let ra = find(parent, a);
            let rb = find(parent, b);
            if ra != rb {
                parent[rb] = ra;
            }
        }

        let mut spf: Vec<usize> = (0..=m).collect();
        let lim = ((m as f64).sqrt() as usize) + 1;
        for i in 2..=lim {
            if spf[i] == i {
                let mut j = i * i;
                while j <= m {
                    if spf[j] == j {
                        spf[j] = i;
                    }
                    j += i;
                }
            }
        }

        let unique: HashSet<i32> = nums.iter().copied().collect();
        for &x in &unique {
            let mut y = x as usize;
            while y > 1 {
                let p = spf[y];
                union(&mut parent, x as usize, p);
                while y % p == 0 {
                    y /= p;
                }
            }
        }

        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();
        for (&a, &b) in nums.iter().zip(sorted_nums.iter()) {
            if find(&mut parent, a as usize) != find(&mut parent, b as usize) {
                return false;
            }
        }
        true
    }
}
