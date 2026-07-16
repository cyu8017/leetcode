// LeetCode 0014 - Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

class Solution {
    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        if (count($strs) === 0) {
            return "";
        }

        $len = strlen($strs[0]);
        for ($i = 0; $i < $len; $i++) {
            $ch = $strs[0][$i];
            for ($j = 1; $j < count($strs); $j++) {
                if ($i >= strlen($strs[$j]) || $strs[$j][$i] !== $ch) {
                    return substr($strs[0], 0, $i);
                }
            }
        }

        return $strs[0];
    }
}
