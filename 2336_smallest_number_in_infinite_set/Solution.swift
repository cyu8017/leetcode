// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

private struct MinHeap {
    private var data: [Int] = []
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ x: Int) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> Int {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty { data[0] = last; siftDown(0) }
        return top
    }
    private mutating func siftUp(_ i: Int) {
        var idx = i
        while idx > 0 {
            let p = (idx - 1) / 2
            if data[p] <= data[idx] { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && data[l] < data[smallest] { smallest = l }
            if r < data.count && data[r] < data[smallest] { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class SmallestInfiniteSet {
    private var next = 1
    private var added = Set<Int>()
    private var heap = MinHeap()

    init() {}

    func popSmallest() -> Int {
        if !heap.isEmpty {
            let x = heap.pop()
            added.remove(x)
            return x
        }
        defer { next += 1 }
        return next
    }

    func addBack(_ num: Int) {
        if num < next && added.insert(num).inserted {
            heap.push(num)
        }
    }
}
