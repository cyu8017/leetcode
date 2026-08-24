// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

impl Solution {
    pub fn count_matching_subarrays(nums: Vec<i32>, pattern: Vec<i32>) -> i32 {
        let npat = pattern.len();
        let mut ps = vec![0i32; npat + 1];
        ps[0] = -1;
        ps[1] = 0;
        let mut p = 0i32;
        for i in 2..=npat {
            let x = pattern[i - 1];
            while p >= 0 && pattern[p as usize] != x {
                p = ps[p as usize];
            }
            p += 1;
            ps[i] = p;
        }
        let mut res = 0;
        let m = nums.len();
        p = 0;
        for i in 1..m {
            let mut t = nums[i] - nums[i - 1];
            if t > 0 {
                t = 1;
            } else if t < 0 {
                t = -1;
            }
            while p >= 0 && pattern[p as usize] != t {
                p = ps[p as usize];
            }
            p += 1;
            if p == npat as i32 {
                res += 1;
                p = ps[p as usize];
            }
        }
        res
    }
}
