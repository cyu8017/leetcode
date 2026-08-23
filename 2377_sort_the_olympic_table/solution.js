// LeetCode 2377 - Sort The Olympic Table
// https://leetcode.com/problems/sort-the-olympic-table/

var QUERY = `SELECT *
FROM Olympic
ORDER BY 2 DESC, 3 DESC, 4 DESC, 1`;

module.exports = { QUERY };
