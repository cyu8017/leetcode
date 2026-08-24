// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

class Solution {
    func totalFruit(_ fruits: [Int]) -> Int {
        var count = [Int: Int]()
        var left = 0, ans = 0
        for right in 0..<fruits.count {
            count[fruits[right], default: 0] += 1
            while count.count > 2 {
                count[fruits[left]]! -= 1
                if count[fruits[left]] == 0 { count.removeValue(forKey: fruits[left]) }
                left += 1
            }
            ans = max(ans, right - left + 1)
        }
        return ans
    }
}
