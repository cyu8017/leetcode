// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

class Solution {
    fun uniqueEmailGroups(emails: Array<String>): Int {
        var st = HashSet<String>()
        for (email in emails) {
            var at = email.indexOf('@')
            var local = email.substring(0, at)
            var domain = email.substring(at + 1).toLowerCase()
            var plus = local.indexOf('+')
            if (plus >= 0) local = local.substring(0, plus)
            var cleaned = StringBuilder()
            for (c in local.toCharArray()) { if (c != '.') cleaned.append(c.lowercaseChar()) }
            st.add(cleaned.toString() + domain)
        }
        return st.size
    }
}
