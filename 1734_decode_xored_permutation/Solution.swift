// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

class Solution {
    func decode(_ encoded: [Int]) -> [Int] {
        let n = encoded.count + 1
        var total = 0
        for value in 1...n {
            total ^= value
        }
        var odd = 0
        var i = 1
        while i < encoded.count {
            odd ^= encoded[i]
            i += 2
        }
        var ans = [total ^ odd]
        for value in encoded {
            ans.append(ans[ans.count - 1] ^ value)
        }
        return ans
    }
}
