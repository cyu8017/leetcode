// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

class Solution {
    fun numUniqueEmails(emails: Array<String>): Int {
        val normalized = HashSet<String>()
        for (email in emails) {
            val at = email.indexOf('@')
            var local = email.substring(0, at)
            val domain = email.substring(at)
            val plus = local.indexOf('+')
            if (plus >= 0) local = local.substring(0, plus)
            val cleaned = StringBuilder()
            for (c in local) if (c != '.') cleaned.append(c)
            normalized.add(cleaned.toString() + domain)
        }
        return normalized.size
    }
}
