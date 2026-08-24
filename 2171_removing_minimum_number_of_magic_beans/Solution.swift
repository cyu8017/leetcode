// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution {
    func minimumRemoval(_ beans: [Int]) -> Int {
        let beans = beans.sorted()
        let n = beans.count
        let sum = beans.reduce(0, +)
        var ans = sum
        for i in 0..<n {
            ans = min(ans, sum - (n - i) * beans[i])
        }
        return ans
    }
}
