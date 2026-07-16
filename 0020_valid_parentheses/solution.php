// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $stack = [];
        $pairs = [
            ')' => '(',
            ']' => '[',
            '}' => '{',
        ];

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch === '(' || $ch === '[' || $ch === '{') {
                $stack[] = $ch;
            } elseif (empty($stack) || array_pop($stack) !== $pairs[$ch]) {
                return false;
            }
        }

        return empty($stack);
    }
}
