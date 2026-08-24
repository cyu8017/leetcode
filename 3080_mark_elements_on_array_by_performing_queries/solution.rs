// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

impl Solution {
    pub fn unmarked_sum_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums.len();
        let mut s: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut mark = vec![false; n];
        let mut arr: Vec<(i32, usize)> = nums.iter().enumerate().map(|(i, &v)| (v, i)).collect();
        arr.sort_unstable();
        let mut ans = vec![0i64; queries.len()];
        let mut j = 0;
        for (qi, q) in queries.iter().enumerate() {
            let index = q[0] as usize;
            let mut k = q[1];
            if !mark[index] {
                mark[index] = true;
                s -= nums[index] as i64;
            }
            while k > 0 && j < n {
                if !mark[arr[j].1] {
                    mark[arr[j].1] = true;
                    s -= arr[j].0 as i64;
                    k -= 1;
                }
                j += 1;
            }
            ans[qi] = s;
        }
        ans
    }
}
