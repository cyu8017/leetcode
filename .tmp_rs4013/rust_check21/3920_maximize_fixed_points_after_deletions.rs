struct Solution;
// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

impl Solution {
    pub fn max_fixed_points(nums: Vec<i32>) -> i32 {
        let mut tails = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if (i as i32) < v {
                continue;
            }
            let d = i as i32 - v;
            match tails.binary_search(&d) {
                Ok(_) => {}
                Err(pos) => {
                    if pos == tails.len() {
                        tails.push(d);
                    } else {
                        tails[pos] = d;
                    }
                }
            }
        }
        tails.len() as i32
    }
}
