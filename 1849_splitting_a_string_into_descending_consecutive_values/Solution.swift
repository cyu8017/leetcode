// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution {
    func splitString(_ s: String) -> Bool {
        let chars = Array(s)
        let n = chars.count

        func normalize(_ digits: [Character]) -> String {
            var i = 0
            while i + 1 < digits.count && digits[i] == "0" { i += 1 }
            return String(digits[i...])
        }

        func compare(_ a: String, _ b: String) -> Int {
            if a.count != b.count { return a.count < b.count ? -1 : 1 }
            if a == b { return 0 }
            return a < b ? -1 : 1
        }

        func subtractOne(_ num: String) -> String {
            var digits = Array(num)
            var i = digits.count - 1
            while i >= 0 {
                if digits[i] != "0" {
                    digits[i] = Character(UnicodeScalar(digits[i].asciiValue! - 1))
                    break
                }
                digits[i] = "9"
                i -= 1
            }
            return normalize(digits)
        }

        func dfs(_ index: Int, _ previous: String?, _ parts: Int) -> Bool {
            if index == n { return parts >= 2 }
            var digits = [Character]()
            for end in index..<n {
                digits.append(chars[end])
                let value = normalize(digits)
                if let previous = previous {
                    let target = subtractOne(previous)
                    let cmp = compare(value, target)
                    if cmp == 0 {
                        if dfs(end + 1, value, parts + 1) { return true }
                    } else if cmp > 0 {
                        break
                    }
                } else {
                    if dfs(end + 1, value, parts + 1) { return true }
                }
            }
            return false
        }

        return dfs(0, nil, 0)
    }
}
