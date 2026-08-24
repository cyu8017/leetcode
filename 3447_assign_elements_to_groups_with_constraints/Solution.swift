// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

class Solution {
    func assignElements(_ groups: [Int], _ elements: [Int]) -> [Int] {
        let maxV = 100001
        var first = Array(repeating: -1, count: maxV)
        for i in 0..<elements.count {
            let e = elements[i]
            if e < maxV && first[e] == -1 { first[e] = i }
        }
        var ans = Array(repeating: -1, count: groups.count)
        for gi in 0..<groups.count {
            let g = groups[gi]
            var best = -1
            var d = 1
            while d * d <= g {
                if g % d == 0 {
                    if first[d] != -1 && (best == -1 || first[d] < best) { best = first[d] }
                    let other = g / d
                    if first[other] != -1 && (best == -1 || first[other] < best) { best = first[other] }
                }
                d += 1
            }
            ans[gi] = best
        }
        return ans
    }
}
