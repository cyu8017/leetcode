// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

class MKAverage {
    private let m: Int
    private let k: Int
    private var stream = [Int]()

    init(_ m: Int, _ k: Int) {
        self.m = m
        self.k = k
    }

    func addElement(_ num: Int) {
        stream.append(num)
    }

    func calculateMKAverage() -> Int {
        if stream.count < m { return -1 }
        let window = Array(stream.suffix(m)).sorted()
        let middle = window[k..<(window.count - k)]
        return middle.reduce(0, +) / middle.count
    }
}
