// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

class Solution {
    func maskPII(_ s: String) -> String {
        if let at = s.firstIndex(of: "@") {
            let lower = s.lowercased()
            let at2 = lower.firstIndex(of: "@")!
            let name = String(lower[..<at2])
            let domain = String(lower[lower.index(after: at2)...])
            return String(name.first!) + "*****" + String(name.last!) + "@" + domain
        }
        let digits = s.filter { $0.isNumber }
        let local = String(digits.suffix(4))
        let country = digits.count - 10
        if country == 0 { return "***-***-" + local }
        return "+" + String(repeating: "*", count: country) + "-***-***-" + local
    }
}
