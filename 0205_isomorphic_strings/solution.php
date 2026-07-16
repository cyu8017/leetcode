// LeetCode 0205 - Isomorphic Strings
// https://leetcode.com/problems/isomorphic-strings/

class Solution {
    function isIsomorphic($s, $t) {
        if (strlen($s) !== strlen($t)) {
            return false;
        }
        $forward = [];
        $backward = [];
        for ($i = 0; $i < strlen($s); $i++) {
            $a = $s[$i];
            $b = $t[$i];
            if ((isset($forward[$a]) && $forward[$a] !== $b)
                || (isset($backward[$b]) && $backward[$b] !== $a)) {
                return false;
            }
            $forward[$a] = $b;
            $backward[$b] = $a;
        }
        return true;
    }
}