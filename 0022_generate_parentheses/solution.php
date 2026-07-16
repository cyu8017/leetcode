// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

class Solution {
    /**
     * @param Integer $n
     * @return String[]
     */
    function generateParenthesis($n) {
        $result = [];
        $path = [];

        $backtrack = function ($openCount, $closeCount) use ($n, &$result, &$path, &$backtrack) {
            if (count($path) === 2 * $n) {
                $result[] = implode('', $path);
                return;
            }
            if ($openCount < $n) {
                $path[] = '(';
                $backtrack($openCount + 1, $closeCount);
                array_pop($path);
            }
            if ($closeCount < $openCount) {
                $path[] = ')';
                $backtrack($openCount, $closeCount + 1);
                array_pop($path);
            }
        };

        $backtrack(0, 0);
        return $result;
    }
}
