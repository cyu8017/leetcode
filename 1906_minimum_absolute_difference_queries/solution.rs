// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

impl Solution {
    pub fn min_difference(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut pref = vec![vec![0i32; 101]; n + 1];
        for (i, &x) in nums.iter().enumerate() {
            pref[i + 1] = pref[i].clone();
            pref[i + 1][x as usize] += 1;
        }
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let left = q[0] as usize;
            let right = q[1] as usize;
            let mut prev = -1;
            let mut best = i32::MAX;
            for value in 1..=100 {
                if pref[right + 1][value] - pref[left][value] > 0 {
                    if prev != -1 {
                        best = best.min(value as i32 - prev);
                    }
                    prev = value as i32;
                }
            }
            ans.push(if best == i32::MAX { -1 } else { best });
        }
        ans
    }
}
