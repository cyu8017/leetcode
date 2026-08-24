// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

class Solution {
    func stableMountains(_ height: [Int], _ threshold: Int) -> [Int] {
        var ans = [Int]()
        for i in 1..<height.count {
            if height[i - 1] > threshold { ans.append(i) }
        }
        return ans
    }
}
