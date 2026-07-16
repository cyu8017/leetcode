// LeetCode 0346 - Moving Average from Data Stream
// https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage {
    private let size: Int
    private var values: [Int] = []
    private var total = 0

    init(_ size: Int) {
        self.size = size
    }

    func next(_ val: Int) -> Double {
        values.append(val)
        total += val
        if values.count > size {
            total -= values.removeFirst()
        }
        return Double(total) / Double(values.count)
    }
}
