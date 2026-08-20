// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution {
    func canBeTypedWords(_ text: String, _ brokenLetters: String) -> Int {
        let broken = Set(brokenLetters)
        return text.split(separator: " ").filter { w in !w.contains(where: { broken.contains($0) }) }.count
    }
}
