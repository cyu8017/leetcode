// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

class Solution {
    func minimumIndex(_ capacity: [Int], _ itemSize: Int) -> Int {
        var ans = -1
        for i in 0..<capacity.count {
            if capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans]) { ans = i }
        }
        return ans
    }
}
