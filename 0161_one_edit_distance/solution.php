// LeetCode 0161 - One Edit Distance
// https://leetcode.com/problems/one-edit-distance/

class Solution {
    function isOneEditDistance(string $s, string $t): bool {
        if (abs(strlen($s) - strlen($t)) > 1 || $s === $t) return false;
        if (strlen($s) > strlen($t)) [$s, $t] = [$t, $s];
        $i = 0;
        while ($i < strlen($s) && $s[$i] === $t[$i]) $i++;
        return strlen($s) === strlen($t)
            ? substr($s, $i + 1) === substr($t, $i + 1)
            : substr($s, $i) === substr($t, $i + 1);
    }
}