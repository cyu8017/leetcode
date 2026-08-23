// LeetCode 1683 - Invalid Tweets
// https://leetcode.com/problems/invalid-tweets/

var QUERY = `SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content)>15`;

module.exports = { QUERY };
