// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

impl Solution {
    fn bit_len(x: u32) -> i32 {
        if x == 0 {
            0
        } else {
            32 - x.leading_zeros() as i32
        }
    }

    pub fn maximum_and(nums: Vec<i32>, k: i32, m: i32) -> i32 {
        let mx_val = *nums.iter().max().unwrap() + k;
        let mx = Self::bit_len(mx_val as u32);
        let mut ans = 0;
        let mut cost = vec![0i32; nums.len()];
        for bit in (0..mx).rev() {
            let target = ans | (1 << bit);
            for i in 0..nums.len() {
                let x = nums[i];
                let j = Self::bit_len((target & !x) as u32);
                let mask = (1 << j) - 1;
                cost[i] = (target & mask) - (x & mask);
            }
            cost.sort_unstable();
            let mut sum = 0;
            for i in 0..m as usize {
                sum += cost[i];
            }
            if sum <= k {
                ans = target;
            }
        }
        ans
    }
}
