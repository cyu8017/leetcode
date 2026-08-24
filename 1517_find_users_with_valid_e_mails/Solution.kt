// LeetCode 1517 - Find Users With Valid E Mails
// https://leetcode.com/problems/find-users-with-valid-e-mails/

class Solution {
    companion object {
        const val QUERY = "SELECT user_id, name, mail\n" +
            "FROM Users\n" +
            "WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$'"
    }
}
