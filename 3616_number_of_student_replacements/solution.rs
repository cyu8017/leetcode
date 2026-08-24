// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

impl Solution {
    pub fn total_replacements(ranks: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut cur = ranks[0];
        for x in ranks {
            if x < cur {
                cur = x;
                ans += 1;
            }
        }
        ans
    }
}
