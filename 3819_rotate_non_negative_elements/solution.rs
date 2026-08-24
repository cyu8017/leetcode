// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

impl Solution {
    pub fn rotate_elements(mut nums: Vec<i32>, k: i32) -> Vec<i32> {
        let t: Vec<i32> = nums.iter().copied().filter(|&x| x >= 0).collect();
        let m = t.len() as i32;
        if m == 0 {
            return nums;
        }
        let mut d = vec![0i32; m as usize];
        for i in 0..m {
            let dest = ((i - k) % m + m) % m;
            d[dest as usize] = t[i as usize];
        }
        let mut j = 0;
        for x in nums.iter_mut() {
            if *x >= 0 {
                *x = d[j];
                j += 1;
            }
        }
        nums
    }
}
