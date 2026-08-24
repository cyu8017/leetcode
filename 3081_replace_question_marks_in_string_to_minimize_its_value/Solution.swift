// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

private struct MinHeap {
    private var data: [(Int, Int)] = []
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
    func minimizeStringValue(_ s: String) -> String {
        var cnt = Array(repeating: 0, count: 26)
        var k = 0
        let chars = Array(s)
        for c in chars {
            if c == "?" { k += 1 }
            else { cnt[Int(c.asciiValue! - Character("a").asciiValue!)] += 1 }
        }
        var pq = MinHeap()
        for i in 0..<26 { pq.push((cnt[i], i)) }
        var t = Array(repeating: 0, count: k)
        for i in 0..<k {
            var p = pq.pop()
            t[i] = p.1
            p.0 += 1
            pq.push(p)
        }
        t.sort()
        var arr = chars
        var j = 0
        let aVal = Character("a").asciiValue!
        for i in 0..<arr.count where arr[i] == "?" {
            arr[i] = Character(UnicodeScalar(aVal + UInt8(t[j])))
            j += 1
        }
        return String(arr)
    }
}
