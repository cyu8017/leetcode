// LeetCode 1747 - Leetflex Banned Accounts
// https://leetcode.com/problems/leetflex-banned-accounts/

var QUERY = `SELECT DISTINCT l1.account_id
FROM LogInfo l1
JOIN LogInfo l2
  ON l1.account_id = l2.account_id
 AND l1.ip_address <> l2.ip_address
 AND l1.login <= l2.logout
 AND l2.login <= l1.logout;`;

module.exports = { QUERY };
