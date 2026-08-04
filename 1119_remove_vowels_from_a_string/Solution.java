// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution {
    public String removeVowels(String s) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u') {
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}
