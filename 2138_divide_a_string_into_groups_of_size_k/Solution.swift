// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution {
    func divideString(_ s: String, _ k: Int, _ fill: Character) -> [String] {
        let chars = Array(s)
        var ans = [String]()
        var i = 0
        while i < chars.count {
            if i + k <= chars.count {
                ans.append(String(chars[i..<(i + k)]))
            } else {
                var chunk = String(chars[i...])
                while chunk.count < k { chunk.append(fill) }
                ans.append(chunk)
            }
            i += k
        }
        return ans
    }
}
