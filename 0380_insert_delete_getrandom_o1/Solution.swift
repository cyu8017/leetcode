// LeetCode 0380 - Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet {
    private var values: [Int] = []
    private var indexByValue: [Int: Int] = [:]

    init() {
    }

    func insert(_ val: Int) -> Bool {
        if indexByValue[val] != nil {
            return false
        }
        indexByValue[val] = values.count
        values.append(val)
        return true
    }

    func remove(_ val: Int) -> Bool {
        guard let index = indexByValue[val] else {
            return false
        }
        let lastValue = values[values.count - 1]
        values[index] = lastValue
        indexByValue[lastValue] = index
        values.removeLast()
        indexByValue.removeValue(forKey: val)
        return true
    }

    func getRandom() -> Int {
        values[Int.random(in: 0..<values.count)]
    }
}
