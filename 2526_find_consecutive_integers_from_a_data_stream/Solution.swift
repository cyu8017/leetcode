// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream {
    private let value: Int
    private let k: Int
    private var streak: Int

    init(_ value: Int, _ k: Int) {
        self.value = value
        self.k = k
        streak = 0
    }

    func consec(_ num: Int) -> Bool {
        if num == value { streak += 1 } else { streak = 0 }
        return streak >= k
    }
}
