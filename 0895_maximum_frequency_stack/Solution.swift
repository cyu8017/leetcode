// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack {
    private var freq = [Int: Int]()
    private var group = [Int: [Int]]()
    private var maxfreq = 0

    init() {}

    func push(_ val: Int) {
        let f = (freq[val] ?? 0) + 1
        freq[val] = f
        maxfreq = max(maxfreq, f)
        group[f, default: []].append(val)
    }

    func pop() -> Int {
        var list = group[maxfreq]!
        let val = list.removeLast()
        group[maxfreq] = list
        freq[val]! -= 1
        if list.isEmpty { maxfreq -= 1 }
        return val
    }
}
