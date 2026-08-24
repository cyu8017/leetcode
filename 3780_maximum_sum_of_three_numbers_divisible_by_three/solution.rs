// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

impl Solution {
    pub fn maximum_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut g: Vec<Vec<i32>> = vec![Vec::new(); 3];
        for x in nums {
            g[(x % 3) as usize].push(x);
        }
        let mut ans = 0;
        for a in 0..3 {
            if !g[a].is_empty() {
                let x = g[a].pop().unwrap();
                for b in 0..3 {
                    if !g[b].is_empty() {
                        let y = g[b].pop().unwrap();
                        let c = (3 - (a + b) % 3) % 3;
                        if !g[c].is_empty() {
                            let z = *g[c].last().unwrap();
                            ans = ans.max(x + y + z);
                        }
                        g[b].push(y);
                    }
                }
                g[a].push(x);
            }
        }
        ans
    }
}
