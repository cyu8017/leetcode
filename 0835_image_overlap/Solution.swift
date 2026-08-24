// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

class Solution {
    func largestOverlap(_ img1: [[Int]], _ img2: [[Int]]) -> Int {
        let n = img1.count
        var ones1 = [(Int, Int)](), ones2 = [(Int, Int)]()
        for i in 0..<n {
            for j in 0..<n {
                if img1[i][j] == 1 { ones1.append((i, j)) }
                if img2[i][j] == 1 { ones2.append((i, j)) }
            }
        }
        if ones1.isEmpty || ones2.isEmpty { return 0 }
        var shifts = [Int: Int]()
        var best = 0
        for a in ones1 {
            for b in ones2 {
                let key = ((a.0 - b.0 + n) << 16) | (a.1 - b.1 + n)
                shifts[key, default: 0] += 1
                best = max(best, shifts[key]!)
            }
        }
        return best
    }
}
