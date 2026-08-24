// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

class Solution {
    private static let POS: [Character: (Int, Int)] = {
        var pos = [Character: (Int, Int)]()
        let keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for i in 0..<3 {
            let row = Array(keys[i])
            for j in 0..<row.count { pos[row[j]] = (i, j) }
        }
        return pos
    }()

    func totalDistance(_ s: String) -> Int {
        var pre: Character = "a"
        var ans = 0
        for cur in s {
            let p1 = Solution.POS[pre]!
            let p2 = Solution.POS[cur]!
            ans += abs(p1.0 - p2.0) + abs(p1.1 - p2.1)
            pre = cur
        }
        return ans
    }
}
