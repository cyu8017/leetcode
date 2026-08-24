// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

impl Solution {
    pub fn sort_even_odd(mut nums: Vec<i32>) -> Vec<i32> {
        let mut even = Vec::new();
        let mut odd = Vec::new();
        for (i, &x) in nums.iter().enumerate() {
            if i % 2 == 0 {
                even.push(x);
            } else {
                odd.push(x);
            }
        }
        even.sort_unstable();
        odd.sort_unstable_by(|a, b| b.cmp(a));
        let mut ei = 0;
        let mut oi = 0;
        for i in 0..nums.len() {
            if i % 2 == 0 {
                nums[i] = even[ei];
                ei += 1;
            } else {
                nums[i] = odd[oi];
                oi += 1;
            }
        }
        nums
    }
}
