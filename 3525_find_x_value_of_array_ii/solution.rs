// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

impl Solution {
    pub fn result_array(mut nums: Vec<i32>, k: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let (idx, val, start, x) = (q[0] as usize, q[1], q[2] as usize, q[3]);
            nums[idx] = val;
            let mut prod = 1;
            let mut cnt = 0;
            for i in start..n {
                prod = prod * (nums[i] % k) % k;
                if prod == x {
                    cnt += 1;
                }
            }
            ans[qi] = cnt;
        }
        ans
    }
}
