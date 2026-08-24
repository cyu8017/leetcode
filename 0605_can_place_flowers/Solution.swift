// LeetCode 0605 - Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

class Solution {
    func canPlaceFlowers(_ flowerbed: [Int], _ n: Int) -> Bool {
        var flowerbed = flowerbed
        var n = n
        if n == 0 { return true }
        for i in 0..<flowerbed.count {
            if flowerbed[i] == 1 { continue }
            let leftEmpty = i == 0 || flowerbed[i - 1] == 0
            let rightEmpty = i == flowerbed.count - 1 || flowerbed[i + 1] == 0
            if leftEmpty && rightEmpty {
                flowerbed[i] = 1
                n -= 1
                if n == 0 { return true }
            }
        }
        return false
    }
}
