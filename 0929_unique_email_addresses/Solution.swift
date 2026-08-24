// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

class Solution {
    func numUniqueEmails(_ emails: [String]) -> Int {
        var normalized = Set<String>()
        for email in emails {
            let at = email.firstIndex(of: "@")!
            var local = String(email[..<at])
            let domain = String(email[at...])
            if let plus = local.firstIndex(of: "+") {
                local = String(local[..<plus])
            }
            local = local.filter { $0 != "." }
            normalized.insert(local + domain)
        }
        return normalized.count
    }
}
