// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

class Solution {
    func maxHammingDistances(_ nums: [Int], _ m: Int) -> [Int] {
        var dist = Array(repeating: -1, count: 1 << m)
        var q: [Int] = []
        for x in nums {
            dist[x] = 0
            q.append(x)
        }
        var k = 1
        while !q.isEmpty {
            var t: [Int] = []
            for x in q {
                for i in 0..<m {
                    let y = x ^ (1 << i)
                    if dist[y] == -1 {
                        dist[y] = k
                        t.append(y)
                    }
                }
            }
            q = t
            k += 1
        }
        return nums.map { x in m - dist[x ^ ((1 << m) - 1)] }
    }
}
