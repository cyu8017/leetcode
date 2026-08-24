// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

class LogSystem {
    private var ids = [Int]()
    private var timestamps = [String]()
    private let granularityIndex = [
        "Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19
    ]

    init() {}

    func put(_ id: Int, _ timestamp: String) {
        ids.append(id)
        timestamps.append(timestamp)
    }

    func retrieve(_ start: String, _ end: String, _ granularity: String) -> [Int] {
        let index = granularityIndex[granularity]!
        let startKey = String(start.prefix(index))
        let endKey = String(end.prefix(index))
        var matched = [(String, Int)]()
        for i in 0..<timestamps.count {
            let key = String(timestamps[i].prefix(index))
            if startKey <= key && key <= endKey {
                matched.append((timestamps[i], ids[i]))
            }
        }
        matched.sort { $0.0 < $1.0 }
        return matched.map { $0.1 }
    }
}
