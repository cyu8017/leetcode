// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo {
    private var books = [(Int, Int)]()
    private var overlaps = [(Int, Int)]()
    init() {}
    func book(_ startTime: Int, _ endTime: Int) -> Bool {
        for (s, e) in overlaps where s < endTime && startTime < e { return false }
        for (s, e) in books where s < endTime && startTime < e {
            overlaps.append((max(s, startTime), min(e, endTime)))
        }
        books.append((startTime, endTime))
        return true
    }
}
