// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

impl Solution {
    pub fn duplicate_numbers_xor(nums: Vec<i32>) -> i32 {
        let mut cnt = [0i32; 51];
        let mut ans = 0;
        for x in nums {
            cnt[x as usize] += 1;
            if cnt[x as usize] == 2 {
                ans ^= x;
            }
        }
        ans
    }
}
