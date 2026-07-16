// LeetCode 0175 - Combine Two Tables
// https://leetcode.com/problems/combine-two-tables/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    Person.firstName,\n"
    "    Person.lastName,\n"
    "    Address.city,\n"
    "    Address.state\n"
    "FROM Person\n"
    "LEFT JOIN Address\n"
    "    ON Person.personId = Address.personId\n";