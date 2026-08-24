// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker {
    private var freq: [Int: Int] = [:]
    private var count: [Int: Int] = [:]

    init() {}

    func add(_ number: Int) {
        let old = freq[number, default: 0]
        if old > 0 { count[old, default: 0] -= 1 }
        freq[number] = old + 1
        count[old + 1, default: 0] += 1
    }

    func deleteOne(_ number: Int) {
        let old = freq[number, default: 0]
        if old == 0 { return }
        count[old, default: 0] -= 1
        freq[number] = old - 1
        if old - 1 > 0 { count[old - 1, default: 0] += 1 }
    }

    func hasFrequency(_ frequency: Int) -> Bool {
        count[frequency, default: 0] > 0
    }
}
