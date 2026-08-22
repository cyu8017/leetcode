// LeetCode 0584 - Find Customer Referee
// https://leetcode.com/problems/find-customer-referee/

const char* QUERY =
    "\n"
    "SELECT name\n"
    "FROM Customer\n"
    "WHERE referee_id != 2 OR referee_id IS NULL\n";
