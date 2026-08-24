// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

class Solution {
    func splitArraySameAverage(_ nums: [Int]) -> Bool {
        let n = nums.count
        let total = nums.reduce(0, +)
        let sorted = nums.sorted()
        var memo = Set<Int>()
        func find(_ target: Int, _ count: Int, _ index: Int) -> Bool {
            if count == 0 { return target == 0 }
            if index == n || count + index > n || target < 0 { return false }
            let key = (target << 20) | (count << 10) | index
            if memo.contains(key) { return false }
            if find(target - sorted[index], count - 1, index + 1) || find(target, count, index + 1) {
                return true
            }
            memo.insert(key)
            return false
        }
        for size in 1..<n {
            if (total * size) % n == 0 && find(total * size / n, size, 0) { return true }
        }
        return false
    }
}
