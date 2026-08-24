// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution {
    func sortVowels(_ s: String) -> String {
        var vowels = Array(s).filter { isVowel($0) }.sorted()
        var arr = Array(s)
        var vi = 0
        for i in arr.indices where isVowel(arr[i]) {
            arr[i] = vowels[vi]
            vi += 1
        }
        return String(arr)
    }

    private func isVowel(_ c: Character) -> Bool {
        "aeiouAEIOU".contains(c)
    }
}
