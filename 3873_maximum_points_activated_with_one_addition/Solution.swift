// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

class Solution {
    private class UnionFind {
        var p = [Int: Int]()
        var size = [Int: Int]()

        func find(_ x: Int) -> Int {
            if p[x] == nil {
                p[x] = x
                size[x] = 1
            }
            if p[x] != x { p[x] = find(p[x]!) }
            return p[x]!
        }

        func unite(_ a: Int, _ b: Int) -> Bool {
            var pa = find(a), pb = find(b)
            if pa == pb { return false }
            if size[pa]! > size[pb]! {
                p[pb] = pa
                size[pa]! += size[pb]!
            } else {
                p[pa] = pb
                size[pb]! += size[pa]!
            }
            return true
        }
    }

    func maxActivated(_ points: [[Int]]) -> Int {
        let uf = UnionFind()
        let m = 3000000000
        for pt in points { _ = uf.unite(pt[0], pt[1] + m) }
        var cnt = [Int: Int]()
        for pt in points {
            let r = uf.find(pt[0])
            cnt[r, default: 0] += 1
        }
        var mx1 = 0, mx2 = 0
        for x in cnt.values {
            if mx1 < x { mx2 = mx1; mx1 = x }
            else if mx2 < x { mx2 = x }
        }
        return mx1 + mx2 + 1
    }
}
