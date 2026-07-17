// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

func mergeAlternately(word1 string, word2 string) string {
    out := make([]byte, 0, len(word1)+len(word2))
    i, j := 0, 0
    for i < len(word1) || j < len(word2) {
        if i < len(word1) {
            out = append(out, word1[i])
            i++
        }
        if j < len(word2) {
            out = append(out, word2[j])
            j++
        }
    }
    return string(out)
}
