// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

impl Solution {
    pub fn bag_of_tokens_score(mut tokens: Vec<i32>, mut power: i32) -> i32 {
        tokens.sort_unstable();
        let mut i = 0i32;
        let mut j = tokens.len() as i32 - 1;
        let mut score = 0;
        let mut ans = 0;
        while i <= j {
            if power >= tokens[i as usize] {
                power -= tokens[i as usize];
                i += 1;
                score += 1;
                ans = ans.max(score);
            } else if score > 0 {
                power += tokens[j as usize];
                j -= 1;
                score -= 1;
            } else {
                break;
            }
        }
        ans
    }
}
