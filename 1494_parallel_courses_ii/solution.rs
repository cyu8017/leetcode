// LeetCode 1494 - Parallel Courses II
// https://leetcode.com/problems/parallel-courses-ii/

impl Solution {
    pub fn min_number_of_semesters(n: i32, relations: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = n as usize;
        let k = k as u32;
        let mut prereq = vec![0usize; n];
        for e in relations {
            prereq[(e[1] - 1) as usize] |= 1 << (e[0] - 1);
        }
        let full = (1 << n) - 1;
        let inf = i32::MAX / 4;
        let mut dp = vec![inf; 1 << n];
        dp[0] = 0;
        for mask in 0..(1 << n) {
            if dp[mask] == inf {
                continue;
            }
            let mut available = 0usize;
            for c in 0..n {
                if mask >> c & 1 == 0 && prereq[c] & mask == prereq[c] {
                    available |= 1 << c;
                }
            }
            let mut choices = Vec::new();
            if available.count_ones() <= k {
                choices.push(available);
            } else {
                let mut sub = available;
                while sub != 0 {
                    if sub.count_ones() == k {
                        choices.push(sub);
                    }
                    sub = (sub - 1) & available;
                }
            }
            for take in choices {
                let nm = mask | take;
                dp[nm] = dp[nm].min(dp[mask] + 1);
            }
        }
        dp[full]
    }
}
