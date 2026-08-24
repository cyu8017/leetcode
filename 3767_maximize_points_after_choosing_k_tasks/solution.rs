// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

impl Solution {
    pub fn max_points(technique1: Vec<i32>, technique2: Vec<i32>, k: i32) -> i64 {
        let n = technique1.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| technique2[i] - technique1[i]);
        let mut ans = 0i64;
        for &x in &technique2 {
            ans += x as i64;
        }
        for i in 0..k as usize {
            let index = idx[i];
            ans -= technique2[index] as i64;
            ans += technique1[index] as i64;
        }
        for i in k as usize..n {
            let index = idx[i];
            if technique1[index] >= technique2[index] {
                ans -= technique2[index] as i64;
                ans += technique1[index] as i64;
            }
        }
        ans
    }
}
