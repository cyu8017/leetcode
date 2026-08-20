// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

class SnapshotArray {
    private var snapId = 0
    private var data: [[[Int]]]

    init(_ length: Int) {
        data = Array(repeating: [[0, 0]], count: length)
    }

    func set(_ index: Int, _ val: Int) {
        var hist = data[index]
        if hist[hist.count - 1][0] == snapId {
            hist[hist.count - 1][1] = val
        } else {
            hist.append([snapId, val])
        }
        data[index] = hist
    }

    func snap() -> Int {
        let id = snapId
        snapId += 1
        return id
    }

    func get(_ index: Int, _ snap_id: Int) -> Int {
        let hist = data[index]
        var lo = 0, hi = hist.count - 1, ans = 0
        while lo <= hi {
            let mid = (lo + hi) / 2
            if hist[mid][0] <= snap_id {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return hist[ans][1]
    }
}
