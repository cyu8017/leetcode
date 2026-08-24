// LeetCode 1683 - Invalid Tweets
// https://leetcode.com/problems/invalid-tweets/

const QUERY: &str = r#"
SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content)>15
"#;
