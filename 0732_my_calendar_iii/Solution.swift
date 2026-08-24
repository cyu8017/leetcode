// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree {
    private var delta = [Int: Int]()
    init() {}
    func book(_ startTime: Int, _ endTime: Int) -> Int {
        delta[startTime, default: 0] += 1
        delta[endTime, default: 0] -= 1
        var cur = 0, best = 0
        for t in delta.keys.sorted() {
            cur += delta[t]!
            best = max(best, cur)
        }
        return best
    }
}
