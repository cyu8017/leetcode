// LeetCode 1310 - XOR Queries of a Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution {
    func xorQueries(_ arr: [Int], _ queries: [[Int]]) -> [Int] {
        var prefix = [0]
        for value in arr { prefix.append(prefix.last! ^ value) }
        return queries.map { prefix[$0[1] + 1] ^ prefix[$0[0]] }
    }
}
