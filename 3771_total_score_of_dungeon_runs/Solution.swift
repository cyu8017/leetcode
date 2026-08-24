// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

class Solution {
    func totalScore(_ hp: Int, _ damage: [Int], _ requirement: [Int]) -> Int {
        let n = damage.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + damage[i] }
        var answer = n * (n + 1) / 2
        for j in 1...n {
            let threshold = prefix[j] + (requirement[j - 1] - hp)
            var lo = 0, hi = j
            while lo < hi {
                let mid = (lo + hi) / 2
                if prefix[mid] < threshold { lo = mid + 1 }
                else { hi = mid }
            }
            answer -= lo
        }
        return answer
    }
}
