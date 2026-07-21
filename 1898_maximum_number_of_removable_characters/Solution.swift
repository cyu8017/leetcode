// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution {
    func maximumRemovals(_ s: String, _ p: String, _ removable: [Int]) -> Int {
        let sArr = Array(s)
        let pArr = Array(p)

        func stillSubsequence(_ k: Int) -> Bool {
            let removed = Set(removable.prefix(k))
            var index = 0
            for (position, char) in sArr.enumerated() {
                if removed.contains(position) {
                    continue
                }
                if index < pArr.count && char == pArr[index] {
                    index += 1
                }
            }
            return index == pArr.count
        }

        var lo = 0
        var hi = removable.count
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if stillSubsequence(mid) {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return lo
    }
}
