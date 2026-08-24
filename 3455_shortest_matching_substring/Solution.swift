// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

class Solution {
    func shortestMatchingSubstring(_ s: String, _ p: String) -> Int {
        var parts = [String]()
        var cur = ""
        for c in p {
            if c == "*" {
                parts.append(cur)
                cur = ""
            } else { cur.append(c) }
        }
        parts.append(cur)
        while parts.count < 3 { parts.append("") }
        let a = parts[0], b = parts[1], c = parts[2]
        let n = s.count
        let posA = findAll(s, a), posB = findAll(s, b), posC = findAll(s, c)
        var ans = n + 1
        for ia in posA {
            let endA = ia + a.count
            var bi = lowerBound(posB, endA)
            if bi < posB.count {
                let endB = posB[bi] + b.count
                let ci = lowerBound(posC, endB)
                if ci < posC.count {
                    let length = posC[ci] + c.count - ia
                    if length < ans { ans = length }
                }
            }
        }
        return ans == n + 1 ? -1 : ans
    }

    private func findAll(_ s: String, _ sub: String) -> [Int] {
        let sa = Array(s), suba = Array(sub)
        var res = [Int]()
        if suba.isEmpty {
            for i in 0...sa.count { res.append(i) }
            return res
        }
        if sa.count >= suba.count {
            for i in 0...(sa.count - suba.count) {
                if Array(sa[i..<(i + suba.count)]) == suba { res.append(i) }
            }
        }
        return res
    }

    private func lowerBound(_ arr: [Int], _ x: Int) -> Int {
        var lo = 0, hi = arr.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if arr[mid] < x { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
