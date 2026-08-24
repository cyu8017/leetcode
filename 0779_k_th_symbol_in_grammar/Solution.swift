// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution {
    func kthGrammar(_ n: Int, _ k: Int) -> Int {
        if n == 1 { return 0 }
        let parent = kthGrammar(n - 1, (k + 1) / 2)
        if parent == 0 { return k % 2 == 1 ? 0 : 1 }
        return k % 2 == 1 ? 1 : 0
    }
}
