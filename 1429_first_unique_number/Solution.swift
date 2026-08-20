// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

class FirstUnique {
    private var counts = [Int: Int]()
    private var unique = [Int]()
    private var uniqueSet = Set<Int>()

    init(_ nums: [Int]) {
        for value in nums { add(value) }
    }

    func showFirstUnique() -> Int {
        while let first = unique.first, counts[first, default: 0] != 1 {
            unique.removeFirst()
            uniqueSet.remove(first)
        }
        return unique.first ?? -1
    }

    func add(_ value: Int) {
        counts[value, default: 0] += 1
        if counts[value] == 1 {
            unique.append(value)
            uniqueSet.insert(value)
        } else {
            uniqueSet.remove(value)
        }
    }
}
