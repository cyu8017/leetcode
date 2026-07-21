// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution {
    func checkIfPangram(_ sentence: String) -> Bool {
        return Set(sentence).count == 26
    }
}
