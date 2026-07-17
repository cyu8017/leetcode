// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

class Solution {
    func decode(_ encoded: [Int], _ first: Int) -> [Int] {
        var ans = [first]
        ans.reserveCapacity(encoded.count + 1)
        for value in encoded {
            ans.append(ans[ans.count - 1] ^ value)
        }
        return ans
    }
}
