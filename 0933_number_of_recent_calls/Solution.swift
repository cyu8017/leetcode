// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter {
    private var q = [Int]()

    init() {}

    func ping(_ t: Int) -> Int {
        q.append(t)
        while !q.isEmpty && q[0] < t - 3000 { q.removeFirst() }
        return q.count
    }
}
