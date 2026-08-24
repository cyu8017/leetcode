// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery {
    private var pos = [Int: [Int]]()

    init(_ arr: [Int]) {
        for i in 0..<arr.count {
            pos[arr[i], default: []].append(i)
        }
    }

    func query(_ left: Int, _ right: Int, _ value: Int) -> Int {
        guard let p = pos[value] else { return 0 }
        return upper(p, right) - lower(p, left)
    }

    private func lower(_ p: [Int], _ x: Int) -> Int {
        var lo = 0, hi = p.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if p[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }

    private func upper(_ p: [Int], _ x: Int) -> Int {
        var lo = 0, hi = p.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if p[mid] <= x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
