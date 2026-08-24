// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

class Solution {
    func goodIndices(_ s: String) -> [Int] {
        let chars = Array(s)
        var ans = [Int]()
        for i in 0..<chars.count {
            let t = String(i)
            let k = t.count
            if i + 1 - k >= 0 && String(chars[(i + 1 - k)..<(i + 1)]) == t {
                ans.append(i)
            }
        }
        return ans
    }
}
