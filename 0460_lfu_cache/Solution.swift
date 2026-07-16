// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

class LFUCache {
    private let capacity: Int
    private var minFreq = 0
    private var keyValues: [Int: Int] = [:]
    private var keyFreqs: [Int: Int] = [:]
    private var freqKeys: [Int: [Int]] = [:]

    init(_ capacity: Int) {
        self.capacity = capacity
    }

    private func touch(_ key: Int) {
        let freq = keyFreqs[key]!
        var bucket = freqKeys[freq] ?? []
        if let index = bucket.firstIndex(of: key) {
            bucket.remove(at: index)
        }
        freqKeys[freq] = bucket
        if bucket.isEmpty && freq == minFreq {
            minFreq += 1
        }
        keyFreqs[key] = freq + 1
        freqKeys[freq + 1, default: []].append(key)
    }

    func get(_ key: Int) -> Int {
        guard let value = keyValues[key] else { return -1 }
        touch(key)
        return value
    }

    func put(_ key: Int, _ value: Int) {
        if capacity == 0 { return }
        if keyValues[key] != nil {
            keyValues[key] = value
            touch(key)
            return
        }

        if keyValues.count >= capacity {
            let evict = freqKeys[minFreq]!.removeFirst()
            keyValues[evict] = nil
            keyFreqs[evict] = nil
        }

        keyValues[key] = value
        keyFreqs[key] = 1
        freqKeys[1, default: []].append(key)
        minFreq = 1
    }
}
