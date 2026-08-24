// LeetCode 3919 - Minimum Cost to Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut s1 = vec![0; n];
        let mut s2 = vec![0; n];
        for i in 1..n {
            let mut c1 = 1;
            if i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1] {
                c1 = nums[i] - nums[i - 1];
            }
            let mut c2 = 1;
            if i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i] {
                c2 = nums[i] - nums[i - 1];
            }
            s1[i] = s1[i - 1] + c1;
            s2[i] = s2[i - 1] + c2;
        }
        queries
            .iter()
            .map(|q| {
                let l = q[0] as usize;
                let r = q[1] as usize;
                if l < r {
                    s1[r] - s1[l]
                } else {
                    s2[l] - s2[r]
                }
            })
            .collect()
    }
}
