// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

class TimeMap {
    private var times: [String: [Int]] = [:]
    private var vals: [String: [String]] = [:]

    init() {}

    func set(_ key: String, _ value: String, _ timestamp: Int) {
        times[key, default: []].append(timestamp)
        vals[key, default: []].append(value)
    }

    func get(_ key: String, _ timestamp: Int) -> String {
        guard let tarr = times[key], let varr = vals[key] else { return "" }
        var lo = 0, hi = tarr.count - 1, ans = -1
        while lo <= hi {
            let mid = (lo + hi) / 2
            if tarr[mid] <= timestamp {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans < 0 ? "" : varr[ans]
    }
}
