// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

impl Solution {
    pub fn calculate_score(s: String) -> i64 {
        let mut stacks = vec![Vec::new(); 26];
        let mut ans = 0i64;
        for (i, ch) in s.bytes().enumerate() {
            let ci = (ch - b'a') as usize;
            let mir = 25 - ci;
            if let Some(j) = stacks[mir].pop() {
                ans += (i - j) as i64;
            } else {
                stacks[ci].push(i);
            }
        }
        ans
    }
}
