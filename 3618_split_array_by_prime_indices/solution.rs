// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

impl Solution {
    pub fn split_array(nums: Vec<i32>) -> i64 {
        const M: usize = 100010;
        let mut p = vec![true; M];
        p[0] = false;
        p[1] = false;
        for i in 2..M {
            if p[i] {
                let mut j = i + i;
                while j < M {
                    p[j] = false;
                    j += i;
                }
            }
        }
        let mut ans: i64 = 0;
        for (i, &x) in nums.iter().enumerate() {
            if p[i] {
                ans += x as i64;
            } else {
                ans -= x as i64;
            }
        }
        ans.abs()
    }
}
