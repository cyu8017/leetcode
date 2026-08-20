// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution {
    func maxNumberOfApples(_ weight: [Int]) -> Int {
        let sorted = weight.sorted()
        var sum = 0, ans = 0
        for w in sorted {
            if sum + w > 5000 { break }
            sum += w
            ans += 1
        }
        return ans
    }
}
