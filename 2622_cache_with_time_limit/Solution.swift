// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

import Dispatch

class TimeLimitedCache {
    private class Entry {
        var value: Int
        var expire: Int64
        init(_ value: Int, _ expire: Int64) {
            self.value = value
            self.expire = expire
        }
    }

    private var data: [Int: Entry] = [:]
    private let start = DispatchTime.now().uptimeNanoseconds

    private func nowMs() -> Int64 {
        Int64((DispatchTime.now().uptimeNanoseconds - start) / 1_000_000)
    }

    func set(_ key: Int, _ value: Int, _ duration: Int) -> Bool {
        let now = nowMs()
        let alive = data[key].map { $0.expire > now } ?? false
        data[key] = Entry(value, now + Int64(duration))
        return alive
    }

    func get(_ key: Int) -> Int {
        let now = nowMs()
        guard let e = data[key], e.expire > now else { return -1 }
        return e.value
    }

    func count() -> Int {
        let now = nowMs()
        var cnt = 0
        var dead: [Int] = []
        for (k, v) in data {
            if v.expire > now { cnt += 1 } else { dead.append(k) }
        }
        for k in dead { data.removeValue(forKey: k) }
        return cnt
    }
}
