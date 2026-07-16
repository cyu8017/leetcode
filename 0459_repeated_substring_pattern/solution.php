// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

class Solution {
    /**
     * @param string $s
     * @return bool
     */
    function repeatedSubstringPattern($s) {
        return $this->repeated_substring_pattern($s);
    }

    /**
     * @param string $s
     * @return bool
     */
    function repeated_substring_pattern($s) {
        $doubled = $s . $s;
        return strpos(substr($doubled, 1, -1), $s) !== false;
    }
}
