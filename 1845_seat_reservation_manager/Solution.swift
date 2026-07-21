// LeetCode 1845 - Seat Reservation Manager
// https://leetcode.com/problems/seat-reservation-manager/

class SeatManager {
    private var available: [Int]

    init(_ n: Int) {
        available = Array(1...n)
        for i in stride(from: available.count / 2 - 1, through: 0, by: -1) {
            siftDown(i)
        }
    }

    func reserve() -> Int {
        let top = available[0]
        let last = available.removeLast()
        if !available.isEmpty {
            available[0] = last
            siftDown(0)
        }
        return top
    }

    func unreserve(_ seatNumber: Int) {
        available.append(seatNumber)
        siftUp(available.count - 1)
    }

    private func siftUp(_ index: Int) {
        var i = index
        while i > 0 {
            let p = (i - 1) / 2
            if available[p] <= available[i] { break }
            available.swapAt(p, i)
            i = p
        }
    }

    private func siftDown(_ index: Int) {
        var i = index
        while true {
            var smallest = i
            let l = 2 * i + 1, r = 2 * i + 2
            if l < available.count && available[l] < available[smallest] { smallest = l }
            if r < available.count && available[r] < available[smallest] { smallest = r }
            if smallest == i { break }
            available.swapAt(i, smallest)
            i = smallest
        }
    }
}
