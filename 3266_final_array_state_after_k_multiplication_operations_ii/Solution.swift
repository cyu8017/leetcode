// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

private struct MinHeap {
    private var data: [(Int, Int)] = []
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ x: (Int, Int)) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> (Int, Int) {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }
    private func less(_ a: (Int, Int), _ b: (Int, Int)) -> Bool {
        a.0 != b.0 ? a.0 < b.0 : a.1 < b.1
    }
    private mutating func siftUp(_ i: Int) {
        var idx = i
        while idx > 0 {
            let p = (idx - 1) / 2
            if !less(data[idx], data[p]) { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && less(data[l], data[smallest]) { smallest = l }
            if r < data.count && less(data[r], data[smallest]) { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class Solution {
    func getFinalState(_ nums: [Int], _ k: Int, _ multiplier: Int) -> [Int] {
        let mod = 1_000_000_007
        if multiplier == 1 { return nums }
        var a = nums
        var rem = k
        var h = MinHeap()
        var maxV = 0
        for i in 0..<a.count {
            h.push((a[i], i))
            maxV = max(maxV, a[i])
        }
        while rem > 0 && !h.isEmpty {
            let (v, i) = h.pop()
            if v * multiplier > maxV && rem >= a.count {
                h.push((v, i))
                break
            }
            let nv = v * multiplier
            a[i] = nv
            maxV = max(maxV, nv)
            h.push((nv, i))
            rem -= 1
        }
        if rem > 0 {
            let n = a.count
            let full = rem / n, r = rem % n
            let powFull = modPow(multiplier, full, mod)
            for i in 0..<n { a[i] = a[i] * powFull % mod }
            var hh = MinHeap()
            for i in 0..<n { hh.push((a[i], i)) }
            for _ in 0..<r {
                let (v0, i) = hh.pop()
                let v = v0 * multiplier % mod
                a[i] = v
                hh.push((v, i))
            }
            for i in 0..<n { a[i] %= mod }
        } else {
            for i in 0..<a.count { a[i] %= mod }
        }
        return a
    }

    private func modPow(_ a0: Int, _ e0: Int, _ mod: Int) -> Int {
        var r = 1, a = a0 % mod, e = e0
        while e > 0 {
            if (e & 1) != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }
}
