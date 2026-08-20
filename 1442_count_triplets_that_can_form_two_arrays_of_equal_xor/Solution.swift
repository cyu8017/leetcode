// LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution {
    func countTriplets(_ arr: [Int]) -> Int {
        var answer = 0
        for i in 0..<arr.count {
            var value = 0
            for k in i..<arr.count {
                value ^= arr[k]
                if value == 0 { answer += k - i }
            }
        }
        return answer
    }
}
