// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

class Solution {
    func minAreaRect(_ points: [[Int]]) -> Int {
        var byX = [Int: [Int]]()
        for p in points { byX[p[0], default: []].append(p[1]) }
        var last = [String: Int]()
        var ans = Int.max
        for x in byX.keys.sorted() {
            let ys = byX[x]!.sorted()
            for i in 0..<ys.count {
                for j in (i + 1)..<ys.count {
                    let key = "\(ys[i])#\(ys[j])"
                    if let prev = last[key] {
                        ans = min(ans, abs(x - prev) * (ys[j] - ys[i]))
                    }
                    last[key] = x
                }
            }
        }
        return ans == Int.max ? 0 : ans
    }
}
