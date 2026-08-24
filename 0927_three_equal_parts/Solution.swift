// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

class Solution {
    func threeEqualParts(_ arr: [Int]) -> [Int] {
        var ones = [Int]()
        for i in 0..<arr.count where arr[i] != 0 { ones.append(i) }
        let n = ones.count
        if n % 3 != 0 { return [-1, -1] }
        if n == 0 { return [0, arr.count - 1] }
        let third = n / 3
        let length = ones.last! - ones[2 * third] + 1
        let a = ones[0], b = ones[third], c = ones[2 * third]
        if a + length > arr.count || b + length > arr.count || c + length > arr.count {
            return [-1, -1]
        }
        for i in 0..<length {
            if arr[a + i] != arr[b + i] || arr[a + i] != arr[c + i] { return [-1, -1] }
        }
        return [a + length - 1, b + length]
    }
}
