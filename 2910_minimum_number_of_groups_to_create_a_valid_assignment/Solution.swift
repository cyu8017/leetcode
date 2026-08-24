// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

class Solution {
    func minGroupsForValidAssignment(_ balls: [Int]) -> Int {
        var freq: [Int: Int] = [:]
        for b in balls { freq[b, default: 0] += 1 }
        let counts = Array(freq.values)
        let minF = counts.min() ?? 1
        for size in stride(from: minF, through: 1, by: -1) {
            var ok = true
            var groups = 0
            for c in counts {
                let rem = c % (size + 1)
                let g2 = c / (size + 1)
                if rem == 0 {
                    groups += g2
                } else if size - rem <= g2 {
                    groups += g2 + 1
                } else {
                    ok = false
                    break
                }
            }
            if ok { return groups }
        }
        return balls.count
    }
}
