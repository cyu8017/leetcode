// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

class Solution {
    func groupStrings(_ words: [String]) -> [Int] {
        var freq = [Int: Int]()
        for w in words {
            var m = 0
            for c in w { m |= 1 << Int(c.asciiValue! - 97) }
            freq[m, default: 0] += 1
        }
        var parent = [Int: Int]()
        var size = [Int: Int]()
        for (m, c) in freq {
            parent[m] = m
            size[m] = c
        }
        func find(_ x: Int) -> Int {
            if parent[x]! != x { parent[x] = find(parent[x]!) }
            return parent[x]!
        }
        func unite(_ a: Int, _ b: Int) {
            var ra = find(a), rb = find(b)
            if ra == rb { return }
            if size[ra]! < size[rb]! { swap(&ra, &rb) }
            parent[rb] = ra
            size[ra]! += size[rb]!
        }
        for m in Array(freq.keys) {
            for b in 0..<26 {
                if (m & (1 << b)) != 0 {
                    let nm = m ^ (1 << b)
                    if freq[nm] != nil { unite(m, nm) }
                    for a in 0..<26 where (nm & (1 << a)) == 0 {
                        let rm = nm | (1 << a)
                        if freq[rm] != nil { unite(m, rm) }
                    }
                } else {
                    let nm = m | (1 << b)
                    if freq[nm] != nil { unite(m, nm) }
                }
            }
        }
        var groups = 0, maxSize = 0
        var seen = Set<Int>()
        for m in freq.keys {
            let r = find(m)
            if seen.insert(r).inserted {
                groups += 1
                maxSize = max(maxSize, size[r]!)
            }
        }
        return [groups, maxSize]
    }
}
