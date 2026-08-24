// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

class Solution {
    func lexSmallestAfterDeletion(_ s: String) -> String {
        var cnt = [Int](repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        var stk = [Character]()
        for c in s {
            while !stk.isEmpty && stk.last! > c && cnt[Int(stk.last!.asciiValue! - 97)] > 1 {
                cnt[Int(stk.last!.asciiValue! - 97)] -= 1
                stk.removeLast()
            }
            stk.append(c)
        }
        while !stk.isEmpty && cnt[Int(stk.last!.asciiValue! - 97)] > 1 {
            cnt[Int(stk.last!.asciiValue! - 97)] -= 1
            stk.removeLast()
        }
        return String(stk)
    }
}
