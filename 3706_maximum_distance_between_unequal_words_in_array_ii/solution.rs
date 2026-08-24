// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

impl Solution {
    pub fn max_distance(words: Vec<String>) -> i32 {
        let n = words.len();
        let mut ans = 0;
        for i in 0..n {
            if words[i] != words[0] {
                ans = ans.max(i as i32 + 1);
            }
            if words[i] != words[n - 1] {
                ans = ans.max((n - i) as i32);
            }
        }
        ans
    }
}
