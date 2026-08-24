// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

class Solution {
    func uniqueEmailGroups(_ emails: [String]) -> Int {
        var st = Set<String>()
        for email in emails {
            let at = email.firstIndex(of: "@")!
            var local = String(email[..<at])
            let domain = email[email.index(after: at)...].lowercased()
            if let plus = local.firstIndex(of: "+") {
                local = String(local[..<plus])
            }
            var cleaned = ""
            for c in local where c != "." { cleaned.append(Character(c.lowercased())) }
            st.insert(cleaned + domain)
        }
        return st.count
    }
}
