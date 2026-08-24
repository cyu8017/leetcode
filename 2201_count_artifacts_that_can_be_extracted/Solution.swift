// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

class Solution {
    func digArtifacts(_ n: Int, _ artifacts: [[Int]], _ dig: [[Int]]) -> Int {
        var dug = Set<Int>()
        for d in dig { dug.insert(d[0] * n + d[1]) }
        var ans = 0
        for a in artifacts {
            var ok = true
            var r = a[0]
            while r <= a[2] && ok {
                var c = a[1]
                while c <= a[3] {
                    if !dug.contains(r * n + c) {
                        ok = false
                        break
                    }
                    c += 1
                }
                r += 1
            }
            if ok { ans += 1 }
        }
        return ans
    }
}
