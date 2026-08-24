// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

class Solution {
    func subdomainVisits(_ cpdomains: [String]) -> [String] {
        var counts = [String: Int]()
        for item in cpdomains {
            let parts = item.split(separator: " ", maxSplits: 1)
            let count = Int(parts[0])!
            var domain = String(parts[1])
            while true {
                counts[domain, default: 0] += count
                if let dot = domain.firstIndex(of: ".") {
                    domain = String(domain[domain.index(after: dot)...])
                } else {
                    break
                }
            }
        }
        return counts.map { "\($0.value) \($0.key)" }
    }
}
