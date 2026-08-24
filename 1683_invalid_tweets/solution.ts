// LeetCode 1683 - Invalid Tweets
// https://leetcode.com/problems/invalid-tweets/

export const QUERY = `SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content)>15`;
