// LeetCode 3150 - Invalid Tweets Ii
// https://leetcode.com/problems/invalid-tweets-ii/

var QUERY = `SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 140
    OR (LENGTH(content) - LENGTH(REPLACE(content, '@', ''))) > 3
    OR (LENGTH(content) - LENGTH(REPLACE(content, '#', ''))) > 3
ORDER BY 1;`;

module.exports = { QUERY };
