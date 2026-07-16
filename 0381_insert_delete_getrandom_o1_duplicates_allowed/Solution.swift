// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

class RandomizedCollection {
    private var values: [Int] = []
    private var indices: [Int: Set<Int>] = [:]

    init() {
    }

    func insert(_ val: Int) -> Bool {
        if indices[val] == nil {
            indices[val] = []
        }
        indices[val]!.insert(values.count)
        values.append(val)
        return indices[val]!.count == 1
    }

    func remove(_ val: Int) -> Bool {
        guard var valueIndices = indices[val], let index = valueIndices.first else {
            return false
        }

        let lastIndex = values.count - 1
        let lastValue = values[lastIndex]
        values[index] = lastValue
        indices[lastValue, default: []].remove(lastIndex)
        indices[lastValue, default: []].insert(index)
        values.removeLast()
        valueIndices.remove(index)
        if valueIndices.isEmpty {
            indices.removeValue(forKey: val)
        } else {
            indices[val] = valueIndices
        }
        return true
    }

    func getRandom() -> Int {
        values[values.count - 1]
    }
}
