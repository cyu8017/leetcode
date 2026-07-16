// LeetCode 0379 - Design Phone Directory
// https://leetcode.com/problems/design-phone-directory/

class PhoneDirectory {
    private var available: Set<Int>

    init(_ maxNumbers: Int) {
        available = Set(0..<maxNumbers)
    }

    func get() -> Int {
        guard let number = available.min() else {
            return -1
        }
        available.remove(number)
        return number
    }

    func check(_ number: Int) -> Bool {
        available.contains(number)
    }

    func release(_ number: Int) {
        available.insert(number)
    }
}
