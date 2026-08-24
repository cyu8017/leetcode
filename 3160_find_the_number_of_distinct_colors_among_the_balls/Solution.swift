// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution {
    func queryResults(_ limit: Int, _ queries: [[Int]]) -> [Int] {
        var g: [Int: Int] = [:]
        var cnt: [Int: Int] = [:]
        return queries.map { q in
            let x = q[0], y = q[1]
            cnt[y, default: 0] += 1
            if let old = g[x] {
                cnt[old]! -= 1
                if cnt[old] == 0 { cnt.removeValue(forKey: old) }
            }
            g[x] = y
            return cnt.count
        }
    }
}
