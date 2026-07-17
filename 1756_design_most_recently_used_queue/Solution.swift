// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

class MRUQueue {
    private var q: [Int]

    init(_ n: Int) {
        q = Array(1...n)
    }

    func fetch(_ k: Int) -> Int {
        let val = q.remove(at: k - 1)
        q.append(val)
        return val
    }
}
