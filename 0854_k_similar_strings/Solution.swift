// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

class Solution {
    func kSimilarity(_ s1: String, _ s2: String) -> Int {
        if s1 == s2 { return 0 }
        let target = Array(s2)
        var queue = [s1]
        var dist = [s1: 0]
        var qi = 0
        func neighbors(_ s: String) -> [String] {
            var arr = Array(s)
            var i = 0
            while arr[i] == target[i] { i += 1 }
            var res = [String]()
            for j in (i + 1)..<arr.count {
                if arr[j] == target[i] && arr[j] != target[j] {
                    arr.swapAt(i, j)
                    res.append(String(arr))
                    arr.swapAt(i, j)
                }
            }
            return res
        }
        while qi < queue.count {
            let cur = queue[qi]
            qi += 1
            let d = dist[cur]!
            for nxt in neighbors(cur) {
                if nxt == s2 { return d + 1 }
                if dist[nxt] == nil {
                    dist[nxt] = d + 1
                    queue.append(nxt)
                }
            }
        }
        return -1
    }
}
