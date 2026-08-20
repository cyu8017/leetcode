// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker {
    private let arr: [Int]
    private var pos: [Int: [Int]] = [:]

    init(_ arr: [Int]) {
        self.arr = arr
        for (i, x) in arr.enumerated() {
            pos[x, default: []].append(i)
        }
    }

    func query(_ left: Int, _ right: Int, _ threshold: Int) -> Int {
        var candidate = 0, count = 0
        for i in left...right {
            if count == 0 { candidate = arr[i] }
            count += arr[i] == candidate ? 1 : -1
        }
        let locs = pos[candidate] ?? []
        let lo = lowerBound(locs, left)
        let hi = upperBound(locs, right)
        return hi - lo >= threshold ? candidate : -1
    }

    private func lowerBound(_ a: [Int], _ t: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < t { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }

    private func upperBound(_ a: [Int], _ t: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] <= t { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
