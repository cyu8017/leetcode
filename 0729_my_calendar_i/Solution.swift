// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

class MyCalendar {
    private var books = [(Int, Int)]()
    init() {}
    func book(_ startTime: Int, _ endTime: Int) -> Bool {
        for (s, e) in books where s < endTime && startTime < e { return false }
        books.append((startTime, endTime))
        return true
    }
}
