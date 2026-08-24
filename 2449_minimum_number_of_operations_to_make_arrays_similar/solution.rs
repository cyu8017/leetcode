// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

impl Solution {
    pub fn make_similar(mut nums: Vec<i32>, mut target: Vec<i32>) -> i64 {
        nums.sort_unstable();
        target.sort_unstable();
        let mut odd_n = Vec::new();
        let mut even_n = Vec::new();
        let mut odd_t = Vec::new();
        let mut even_t = Vec::new();
        for x in nums {
            if x % 2 == 0 {
                even_n.push(x);
            } else {
                odd_n.push(x);
            }
        }
        for x in target {
            if x % 2 == 0 {
                even_t.push(x);
            } else {
                odd_t.push(x);
            }
        }
        let mut ans = 0i64;
        for i in 0..odd_n.len() {
            let diff = odd_n[i] - odd_t[i];
            if diff > 0 {
                ans += (diff / 2) as i64;
            }
        }
        for i in 0..even_n.len() {
            let diff = even_n[i] - even_t[i];
            if diff > 0 {
                ans += (diff / 2) as i64;
            }
        }
        ans
    }
}
