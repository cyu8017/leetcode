// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

class Solution {
    func accountsMerge(_ accounts: [[String]]) -> [[String]] {
        var parent = [String: String]()
        func find(_ x: String) -> String {
            parent[x] = parent[x] ?? x
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]!]
                x = parent[x]!
            }
            return x
        }
        func unite(_ a: String, _ b: String) { parent[find(a)] = find(b) }
        var emailName = [String: String]()
        for account in accounts {
            let name = account[0], first = account[1]
            for i in 1..<account.count {
                let email = account[i]
                parent[email] = parent[email] ?? email
                emailName[email] = name
                unite(first, email)
            }
        }
        var groups = [String: [String]]()
        for email in parent.keys {
            groups[find(email), default: []].append(email)
        }
        return groups.values.map { emails in
            [emailName[emails[0]]!] + emails.sorted()
        }
    }
}
