// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

class MapSum {
    private var values = [String: Int]()
    private var prefixSums = [String: Int]()

    init() {}

    func insert(_ key: String, _ val: Int) {
        let delta = val - (values[key] ?? 0)
        values[key] = val
        for i in 1...key.count {
            let prefix = String(key.prefix(i))
            prefixSums[prefix, default: 0] += delta
        }
    }

    func sum(_ prefix: String) -> Int {
        prefixSums[prefix] ?? 0
    }
}
