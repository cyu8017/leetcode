// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

class Solution {
    func lexSmallest(_ s: String) -> String {
        var ans = s
        let n = s.count
        for k in 1...n {
            var a1 = Array(s)
            reverse(&a1, 0, k)
            let t1 = String(a1)
            var a2 = Array(s)
            reverse(&a2, n - k, n)
            let t2 = String(a2)
            if t1 < ans { ans = t1 }
            if t2 < ans { ans = t2 }
        }
        return ans
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
