// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

private struct MinHeap<T: Comparable> {
    private var data: [T] = []
    var isEmpty: Bool { data.isEmpty }
    func peek() -> T { data[0] }
    mutating func push(_ x: T) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> T {
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

private struct Busy: Comparable {
    let end: Int
    let room: Int
    static func < (lhs: Busy, rhs: Busy) -> Bool {
        if lhs.end != rhs.end { return lhs.end < rhs.end }
        return lhs.room < rhs.room
    }
}

class Solution {
    func mostBooked(_ n: Int, _ meetings: [[Int]]) -> Int {
        let meetings = meetings.sorted { $0[0] < $1[0] }
        var free = MinHeap<Int>()
        for i in 0..<n { free.push(i) }
        var busy = MinHeap<Busy>()
        var cnt = [Int](repeating: 0, count: n)
        for m in meetings {
            let start = m[0], end = m[1]
            while !busy.isEmpty && busy.peek().end <= start {
                free.push(busy.pop().room)
            }
            let dur = end - start
            let room: Int
            let begin: Int
            if !free.isEmpty {
                room = free.pop()
                begin = start
            } else {
                let top = busy.pop()
                begin = top.end
                room = top.room
            }
            busy.push(Busy(end: begin + dur, room: room))
            cnt[room] += 1
        }
        var ans = 0
        for i in 1..<n where cnt[i] > cnt[ans] { ans = i }
        return ans
    }
}
