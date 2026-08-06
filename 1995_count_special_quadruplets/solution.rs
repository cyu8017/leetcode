// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for a in 0..n {
            for b in (a + 1)..n {
                for c in (b + 1)..n {
                    let s = nums[a] + nums[b] + nums[c];
                    for d in (c + 1)..n {
                        if nums[d] == s {
                            ans += 1;
                        }
                    }
                }
            }
        }
        ans
    }
}
