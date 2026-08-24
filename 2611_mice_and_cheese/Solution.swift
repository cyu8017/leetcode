// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

class Solution {
    func miceAndCheese(_ reward1: [Int], _ reward2: [Int], _ k: Int) -> Int {
        let n = reward1.count
        var ans = 0
        var diff = [Int]()
        for i in 0..<n {
            ans += reward2[i]
            diff.append(reward1[i] - reward2[i])
        }
        diff.sort(by: >)
        if k > 0 {
            for i in 0..<k { ans += diff[i] }
        }
        return ans
    }
}
