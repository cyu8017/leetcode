// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

class Solution {
    func toggleLightBulbs(_ bulbs: [Int]) -> [Int] {
        var st = [Int](repeating: 0, count: 101)
        for x in bulbs { st[x] ^= 1 }
        var ans = [Int]()
        for i in 0..<101 where st[i] == 1 { ans.append(i) }
        return ans
    }
}
