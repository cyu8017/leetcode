// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

class Solution {
    func countTriples(_ n: Int) -> Int {
        var squares = Set<Int>()
        for i in 1...n { squares.insert(i * i) }
        var ans = 0
        for a in 1...n {
            for b in 1...n {
                if squares.contains(a * a + b * b) { ans += 1 }
            }
        }
        return ans
    }
}
