// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

class Solution {
    func lexSmallest(_ s: String) -> String {
        let n = s.count
        var best = s
        if n >= 1 {
            for i in 1...n {
                var t = Array(s)
                reverse(&t, 0, i)
                let ts = String(t)
                if ts < best { best = ts }
            }
        }
        for i in 0..<n {
            var t = Array(s)
            reverse(&t, i, n)
            let ts = String(t)
            if ts < best { best = ts }
        }
        return best
    }

    private func reverse(_ a: inout [Character], _ l: Int, _ r: Int) {
        var i = l, j = r - 1
        while i < j {
            a.swapAt(i, j)
            i += 1
            j -= 1
        }
    }
}
