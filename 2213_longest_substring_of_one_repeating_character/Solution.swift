// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

private struct Seg {
    var lChar: Character = " "
    var rChar: Character = " "
    var lLen = 0, rLen = 0, best = 0, size = 0
}

class Solution {
    private func merge(_ a: Seg, _ b: Seg) -> Seg {
        if a.size == 0 { return b }
        if b.size == 0 { return a }
        var res = Seg()
        res.lChar = a.lChar
        res.rChar = b.rChar
        res.size = a.size + b.size
        res.best = max(a.best, b.best)
        res.lLen = a.lLen
        res.rLen = b.rLen
        if a.rChar == b.lChar {
            let mid = a.rLen + b.lLen
            res.best = max(res.best, mid)
            if a.lLen == a.size { res.lLen = a.size + b.lLen }
            if b.rLen == b.size { res.rLen = b.size + a.rLen }
        }
        return res
    }

    func longestRepeating(_ s: String, _ queryCharacters: String, _ queryIndices: [Int]) -> [Int] {
        var arr = Array(s)
        let n = arr.count
        var tree = [Seg](repeating: Seg(), count: 4 * n + 5)
        func build(_ idx: Int, _ l: Int, _ r: Int) {
            if l == r {
                tree[idx] = Seg(lChar: arr[l], rChar: arr[l], lLen: 1, rLen: 1, best: 1, size: 1)
                return
            }
            let mid = (l + r) / 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1])
        }
        func update(_ idx: Int, _ l: Int, _ r: Int, _ pos: Int, _ ch: Character) {
            if l == r {
                arr[pos] = ch
                tree[idx] = Seg(lChar: ch, rChar: ch, lLen: 1, rLen: 1, best: 1, size: 1)
                return
            }
            let mid = (l + r) / 2
            if pos <= mid { update(idx * 2, l, mid, pos, ch) }
            else { update(idx * 2 + 1, mid + 1, r, pos, ch) }
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1])
        }
        build(1, 0, n - 1)
        let qc = Array(queryCharacters)
        var ans = [Int](repeating: 0, count: queryIndices.count)
        for i in 0..<queryIndices.count {
            update(1, 0, n - 1, queryIndices[i], qc[i])
            ans[i] = tree[1].best
        }
        return ans
    }
}
