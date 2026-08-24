// LeetCode 3799 - Word Squares II
// https://leetcode.com/problems/word-squares-ii/

class Solution {
    func wordSquares(_ words: [String]) -> [[String]] {
        let words = words.sorted()
        let n = words.count
        var ans = [[String]]()
        for i in 0..<n {
            let top = Array(words[i])
            for j in 0..<n where j != i {
                let left = Array(words[j])
                for k in 0..<n where k != j && k != i {
                    let right = Array(words[k])
                    for h in 0..<n where h != k && h != j && h != i {
                        let bottom = Array(words[h])
                        if top[0] == left[0] && top[3] == right[0] &&
                            bottom[0] == left[3] && bottom[3] == right[3] {
                            ans.append([words[i], words[j], words[k], words[h]])
                        }
                    }
                }
            }
        }
        return ans
    }
}
