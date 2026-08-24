// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

class Solution {
    func kEmptySlots(_ bulbs: [Int], _ k: Int) -> Int {
        let n = bulbs.count
        var days = Array(repeating: 0, count: n)
        for day in 1...n { days[bulbs[day - 1] - 1] = day }
        var ans = Int.max
        var i = 0
        while i < n - k - 1 {
            let left = i, right = i + k + 1
            var j = left + 1
            while j < right && days[j] > days[left] && days[j] > days[right] { j += 1 }
            if j == right {
                ans = min(ans, max(days[left], days[right]))
                i += 1
            } else {
                i = j
            }
        }
        return ans == Int.max ? -1 : ans
    }
}
