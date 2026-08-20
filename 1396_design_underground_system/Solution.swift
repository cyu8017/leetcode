// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

class UndergroundSystem {
    private var ins = [Int: (String, Int)]()
    private var stats = [String: (Int, Int)]()

    init() {}

    func checkIn(_ id: Int, _ stationName: String, _ t: Int) {
        ins[id] = (stationName, t)
    }

    func checkOut(_ id: Int, _ stationName: String, _ t: Int) {
        let (start, begin) = ins.removeValue(forKey: id)!
        let key = start + ">" + stationName
        let (total, count) = stats[key, default: (0, 0)]
        stats[key] = (total + t - begin, count + 1)
    }

    func getAverageTime(_ startStation: String, _ endStation: String) -> Double {
        let (total, count) = stats[startStation + ">" + endStation]!
        return Double(total) / Double(count)
    }
}
