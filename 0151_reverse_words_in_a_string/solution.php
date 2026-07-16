// LeetCode 0151 - Reverse Words in a String
// https://leetcode.com/problems/reverse-words-in-a-string/

class Solution {
    function reverseWords(string $s): string {
        $words = preg_split('/\s+/', trim($s));
        if ($words === false || $words === ['']) {
            return '';
        }
        return implode(' ', array_reverse($words));
    }
}