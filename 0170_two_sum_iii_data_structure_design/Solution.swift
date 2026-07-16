// LeetCode 0170 - Two Sum III - Data structure design
// https://leetcode.com/problems/two-sum-iii-data-structure-design/

class TwoSum {
    private var counts = [Int: Int]()

    func add(_ number: Int) {
        counts[number, default: 0] += 1
    }

    func find(_ value: Int) -> Bool {
        for (number, count) in counts {
            let complement = value - number
            if complement == number {
                if count >= 2 { return true }
            } else if counts[complement] != nil {
                return true
            }
        }
        return false
    }
}