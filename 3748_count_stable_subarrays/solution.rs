// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

impl Solution {
    pub fn count_stable_subarrays(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums.len();
        let mut seg = Vec::new();
        let mut s = vec![0i64];
        let mut l = 0usize;
        for r in 0..n {
            if r == n - 1 || nums[r] > nums[r + 1] {
                seg.push(l as i32);
                let k = (r - l + 1) as i64;
                s.push(s.last().unwrap() + k * (k + 1) / 2);
                l = r + 1;
            }
        }
        let mut ans = vec![0i64; queries.len()];
        for (idx, q) in queries.iter().enumerate() {
            let left = q[0];
            let right = q[1];
            let i = seg.partition_point(|&x| x < left + 1);
            let j = seg.partition_point(|&x| x < right + 1) as i32 - 1;
            if i as i32 > j {
                let k = (right - left + 1) as i64;
                ans[idx] = k * (k + 1) / 2;
            } else {
                let a = seg[i] as i64 - left as i64;
                let b = right as i64 - seg[j as usize] as i64 + 1;
                ans[idx] = a * (a + 1) / 2 + s[j as usize] - s[i] + b * (b + 1) / 2;
            }
        }
        ans
    }
}
