// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution {
    func groupThePeople(_ groupSizes: [Int]) -> [[Int]] {
        var buckets: [Int: [Int]] = [:]
        var ans: [[Int]] = []
        for (i, size) in groupSizes.enumerated() {
            buckets[size, default: []].append(i)
            if buckets[size]!.count == size {
                ans.append(buckets[size]!)
                buckets[size] = []
            }
        }
        return ans
    }
}
