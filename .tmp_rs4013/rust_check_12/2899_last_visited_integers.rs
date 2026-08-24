struct Solution;
// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

impl Solution {
    pub fn last_visited_integers(nums: Vec<i32>) -> Vec<i32> {
        let mut seen = Vec::new();
        let mut ans = Vec::new();
        let mut k = 0usize;
        for v in nums {
            if v != -1 {
                seen.push(v);
                k = 0;
            } else {
                k += 1;
                if k > seen.len() {
                    ans.push(-1);
                } else {
                    ans.push(seen[seen.len() - k]);
                }
            }
        }
        ans
    }
}

fn main() {}
