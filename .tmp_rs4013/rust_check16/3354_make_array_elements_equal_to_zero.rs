struct Solution;
// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

impl Solution {
    pub fn count_valid_selections(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            if nums[i] != 0 {
                continue;
            }
            for dir in [-1, 1] {
                let mut a = nums.clone();
                let mut cur = i as i32;
                let mut d = dir;
                while cur >= 0 && cur < n as i32 {
                    if a[cur as usize] == 0 {
                        cur += d;
                    } else {
                        a[cur as usize] -= 1;
                        d = -d;
                        cur += d;
                    }
                }
                if a.iter().all(|&v| v == 0) {
                    ans += 1;
                }
            }
        }
        ans
    }
}

fn main() {}
