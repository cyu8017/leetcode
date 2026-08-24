// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

class ExamRoom {
    private let n: Int
    private var seats = [Int]()

    init(_ n: Int) {
        self.n = n
    }

    func seat() -> Int {
        if seats.isEmpty {
            seats.append(0)
            return 0
        }
        var bestSeat = 0
        var bestDist = seats[0]
        var prev = seats[0]
        for cur in seats {
            if cur == prev { continue }
            let dist = (cur - prev) / 2
            if dist > bestDist {
                bestDist = dist
                bestSeat = prev + dist
            }
            prev = cur
        }
        if n - 1 - seats.last! > bestDist { bestSeat = n - 1 }
        seats.append(bestSeat)
        seats.sort()
        return bestSeat
    }

    func leave(_ p: Int) {
        if let idx = seats.firstIndex(of: p) { seats.remove(at: idx) }
    }
}
