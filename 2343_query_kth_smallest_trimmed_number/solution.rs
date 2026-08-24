// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

impl Solution {
    pub fn smallest_trimmed_numbers(nums: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = vec![0; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let k = q[0] as usize;
            let trim = q[1] as usize;
            let mut arr: Vec<(String, i32)> = nums
                .iter()
                .enumerate()
                .map(|(i, s)| (s[s.len() - trim..].to_string(), i as i32))
                .collect();
            arr.sort_by(|a, b| {
                if a.0 == b.0 {
                    a.1.cmp(&b.1)
                } else {
                    a.0.cmp(&b.0)
                }
            });
            ans[qi] = arr[k - 1].1;
        }
        ans
    }
}
