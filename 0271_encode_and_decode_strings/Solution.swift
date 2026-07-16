// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

class Codec {
    func encode(_ strs: [String]) -> String {
        strs.map { "\($0.count)#\($0)" }.joined()
    }

    func decode(_ encoded: String) -> [String] {
        var result: [String] = []
        var index = encoded.startIndex
        while index < encoded.endIndex {
            guard let delimiter = encoded[index...].firstIndex(of: "#") else { break }
            let length = Int(encoded[index..<delimiter])!
            let start = encoded.index(after: delimiter)
            let end = encoded.index(start, offsetBy: length)
            result.append(String(encoded[start..<end]))
            index = end
        }
        return result
    }
}
