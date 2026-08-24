// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

class Solution {
    func maxSubstringLength(_ s: String, _ k: Int) -> Bool {
        let chars = Array(s)
        let n = chars.count
        var first = Array(repeating: n, count: 26)
        var last = Array(repeating: -1, count: 26)
        for i in 0..<n {
            let ci = Int(chars[i].asciiValue! - 97)
            if first[ci] == n { first[ci] = i }
            last[ci] = i
        }
        var segs = [[Int]]()
        for c in 0..<26 {
            if last[c] == -1 { continue }
            var l = first[c], r = last[c]
            var i = l
            while i <= r {
                let ci = Int(chars[i].asciiValue! - 97)
                if first[ci] < l {
                    l = first[ci]
                    i = l
                    continue
                }
                if last[ci] > r { r = last[ci] }
                i += 1
            }
            if !(l == 0 && r == n - 1) { segs.append([l, r]) }
        }
        var uniq = Set<Int>()
        var arr = [[Int]]()
        for sg in segs {
            let key = (sg[0] << 32) | (sg[1] & ((1 << 32) - 1))
            if uniq.insert(key).inserted { arr.append(sg) }
        }
        arr.sort { $0[1] < $1[1] }
        var cnt = 0, end = -1
        for sg in arr where sg[0] > end {
            cnt += 1
            end = sg[1]
        }
        return cnt >= k
    }
}
