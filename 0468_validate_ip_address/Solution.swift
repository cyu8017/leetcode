// LeetCode 0468 - Validate IP Address
// https://leetcode.com/problems/validate-ip-address/

class Solution {
    func validIPAddress(_ queryIP: String) -> String {
        if isIPv4(queryIP) {
            return "IPv4"
        }
        if isIPv6(queryIP) {
            return "IPv6"
        }
        return "Neither"
    }

    private func isIPv4(_ address: String) -> Bool {
        let parts = address.split(separator: ".", omittingEmptySubsequences: false).map(String.init)
        if parts.count != 4 {
            return false
        }

        for part in parts {
            guard part.allSatisfy({ $0.isNumber }) else {
                return false
            }
            if part.count > 1 && part.first == "0" {
                return false
            }
            if part.isEmpty || part.count > 3 {
                return false
            }
            guard let value = Int(part), value <= 255 else {
                return false
            }
        }

        return true
    }

    private func isIPv6(_ address: String) -> Bool {
        let parts = address.split(separator: ":", omittingEmptySubsequences: false).map(String.init)
        if parts.count != 8 {
            return false
        }

        let hexDigits = CharacterSet(charactersIn: "0123456789abcdefABCDEF")
        for part in parts {
            if part.isEmpty || part.count > 4 {
                return false
            }
            if part.unicodeScalars.contains(where: { !hexDigits.contains($0) }) {
                return false
            }
        }

        return true
    }
}
