// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n == 1 {
            return true;
        }
        let mx = *nums.iter().max().unwrap() as usize;
        let mut parent: Vec<usize> = (0..=mx).collect();
        fn find(parent: &mut [usize], mut x: usize) -> usize {
            while parent[x] != x {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            x
        }
        let unite = |parent: &mut [usize], a: usize, b: usize| {
            let ra = find(parent, a);
            let rb = find(parent, b);
            if ra != rb {
                parent[ra] = rb;
            }
        };
        let mut has = vec![false; mx + 1];
        for &x in &nums {
            if x == 1 {
                return false;
            }
            has[x as usize] = true;
        }
        let mut sieve = vec![0usize; mx + 1];
        for i in 2..=mx {
            if sieve[i] == 0 {
                let mut j = i;
                while j <= mx {
                    if sieve[j] == 0 {
                        sieve[j] = i;
                    }
                    if has[j] {
                        unite(&mut parent, i, j);
                    }
                    j += i;
                }
            }
        }
        let root = find(&mut parent, nums[0] as usize);
        for &x in &nums {
            if find(&mut parent, x as usize) != root {
                return false;
            }
        }
        true
    }
}
