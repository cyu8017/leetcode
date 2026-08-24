struct Solution;
fn main() {}

// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

impl Solution {
    pub fn check_array(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        let k = k as usize;
        let mut diff = vec![0i32; n + 1];
        let mut cur = 0;
        for i in 0..n {
            cur += diff[i];
            let need = nums[i] - cur;
            if need < 0 {
                return false;
            }
            if need > 0 {
                if i + k > n {
                    return false;
                }
                cur += need;
                diff[i + k] -= need;
            }
        }
        true
    }
}
