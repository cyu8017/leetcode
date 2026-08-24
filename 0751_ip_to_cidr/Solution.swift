// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

class Solution {
    func ipToCIDR(_ ip: String, _ n: Int) -> [String] {
        var start = ipToInt(ip)
        var n = n
        var answer = [String]()
        while n > 0 {
            var lowbit = start == 0 ? (1 << 32) : (start & -start)
            while lowbit > n { lowbit >>= 1 }
            let mask = 32 - (bitLength(lowbit) - 1)
            answer.append(intToIp(start) + "/\(mask)")
            start += lowbit
            n -= lowbit
        }
        return answer
    }

    private func ipToInt(_ value: String) -> Int {
        value.split(separator: ".").reduce(0) { $0 * 256 + Int($1)! }
    }

    private func intToIp(_ value: Int) -> String {
        "\((value >> 24) & 255).\((value >> 16) & 255).\((value >> 8) & 255).\(value & 255)"
    }

    private func bitLength(_ value: Int) -> Int {
        var value = value, len = 0
        while value > 0 { value >>= 1; len += 1 }
        return len
    }
}
