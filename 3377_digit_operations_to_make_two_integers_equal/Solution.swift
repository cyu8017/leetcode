// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

private struct MinHeap2 {
    private var a: [(Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].0 <= a[i].0 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && a[l].0 < a[s].0 { s = l }
                if rg < a.count && a[rg].0 < a[s].0 { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}

class Solution {
    func minOperations(_ n: Int, _ m: Int) -> Int {
        var isPrime = Array(repeating: false, count: 100000)
        if 2 < 100000 {
            for i in 2..<100000 { isPrime[i] = true }
        }
        var i = 2
        while i * i < 100000 {
            if isPrime[i] {
                var j = i * i
                while j < 100000 {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        if isPrime[n] { return -1 }
        var dist = Array(repeating: -1, count: 100000)
        var pq = MinHeap2()
        pq.push((n, n))
        dist[n] = n
        while !pq.isEmpty {
            let (cost, val) = pq.pop()
            if cost != dist[val] { continue }
            if val == m { return cost }
            var s = Array(String(val))
            for i in 0..<s.count {
                let orig = s[i]
                for d in [-1, 1] {
                    let nd = Int(orig.asciiValue! - 48) + d
                    if nd < 0 || nd > 9 { continue }
                    if i == 0 && nd == 0 && s.count > 1 { continue }
                    s[i] = Character(UnicodeScalar(nd + 48)!)
                    let nv = Int(String(s))!
                    s[i] = orig
                    if isPrime[nv] { continue }
                    let nc = cost + nv
                    if dist[nv] == -1 || nc < dist[nv] {
                        dist[nv] = nc
                        pq.push((nc, nv))
                    }
                }
            }
        }
        return -1
    }
}
