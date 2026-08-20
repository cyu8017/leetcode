// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

class Solution {
    func findSmallestRegion(_ regions: [[String]], _ region1: String, _ region2: String) -> String {
        var parent: [String: String] = [:]
        for r in regions {
            for i in 1..<r.count { parent[r[i]] = r[0] }
        }
        var seen = Set<String>()
        var cur: String? = region1
        while let c = cur {
            seen.insert(c)
            cur = parent[c]
        }
        cur = region2
        while let c = cur {
            if seen.contains(c) { return c }
            cur = parent[c]
        }
        return region1
    }
}
