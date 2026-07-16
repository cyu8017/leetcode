// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

class Solution {
    func encode(_ s: String) -> String {
        let chars = Array(s)
        let length = chars.count
        var dp = Array(repeating: "", count: length + 1)

        func encodeWord(_ word: [Character]) -> String {
            let size = word.count
            var best = String(word)
            var unitLength = 1
            while unitLength <= size / 2 {
                if size % unitLength == 0 {
                    let unit = word[0..<unitLength]
                    let repeated = String(repeating: String(unit), count: size / unitLength)
                    if repeated == String(word) {
                        let encoded = "\(size / unitLength)[\(String(unit))]"
                        if encoded.count < best.count || (encoded.count == best.count && encoded < best) {
                            best = encoded
                        }
                    }
                }
                unitLength += 1
            }
            return best
        }

        var index = 1
        while index <= length {
            dp[index] = encodeWord(Array(chars[0..<index]))
            var split = 1
            while split < index {
                let candidate = dp[index - split] + encodeWord(Array(chars[(index - split)..<index]))
                if candidate.count < dp[index].count || (candidate.count == dp[index].count && candidate < dp[index]) {
                    dp[index] = candidate
                }
                split += 1
            }
            index += 1
        }
        return dp[length]
    }
}
