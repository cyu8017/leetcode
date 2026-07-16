// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

class Solution {
    func restoreIpAddresses(_ s: String) -> [String] {
        let chars = Array(s)
        var result: [String] = []
        var path: [String] = []

        func backtrack(_ start: Int) {
            if path.count == 4 {
                if start == chars.count {
                    result.append(path.joined(separator: "."))
                }
                return
            }

            for length in 1...3 {
                if start + length > chars.count {
                    break
                }
                let part = String(chars[start..<(start + length)])
                if (part.hasPrefix("0") && part.count > 1) || Int(part)! > 255 {
                    continue
                }
                path.append(part)
                backtrack(start + length)
                path.removeLast()
            }
        }

        backtrack(0)
        return result
    }
}
