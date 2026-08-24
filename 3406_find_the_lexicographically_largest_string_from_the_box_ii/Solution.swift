// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

class Solution {
    func answerString(_ word: String, _ numFriends: Int) -> String {
        if numFriends == 1 { return word }
        let w = Array(word)
        let n = w.count
        let maxLen = n - (numFriends - 1)
        var ans = ""
        for i in 0..<n {
            var end = i + maxLen
            if end > n { end = n }
            let cand = String(w[i..<end])
            if cand > ans { ans = cand }
        }
        return ans
    }
}
