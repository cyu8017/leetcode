// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution {
    func avoidFlood(_ rains: [Int]) -> [Int] {
        var ans = Array(repeating: -1, count: rains.count)
        var full = [Int: Int](), dry = [Int]()
        for (i, lake) in rains.enumerated() {
            if lake == 0 {
                dry.append(i); ans[i] = 1
            } else {
                if let prev = full[lake] {
                    guard let j = dry.firstIndex(where: { $0 > prev }) else { return [] }
                    ans[dry.remove(at: j)] = lake
                }
                full[lake] = i
            }
        }
        return ans
    }
}
