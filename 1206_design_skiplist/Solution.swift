// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

class Skiplist {
    private var values: [Int] = []

    func search(_ target: Int) -> Bool {
        values.contains(target)
    }

    func add(_ num: Int) {
        let i = values.firstIndex { $0 >= num } ?? values.count
        values.insert(num, at: i)
    }

    func erase(_ num: Int) -> Bool {
        if let i = values.firstIndex(of: num) {
            values.remove(at: i)
            return true
        }
        return false
    }
}
