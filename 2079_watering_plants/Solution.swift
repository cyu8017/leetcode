// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

class Solution {
    func wateringPlants(_ plants: [Int], _ capacity: Int) -> Int {
        var ans = 0, cur = capacity
        for i in 0..<plants.count {
            if cur < plants[i] {
                ans += i * 2
                cur = capacity
            }
            cur -= plants[i]
            ans += 1
        }
        return ans
    }
}
