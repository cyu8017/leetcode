// LeetCode 0165 - Compare Version Numbers
// https://leetcode.com/problems/compare-version-numbers/

class Solution {
    function compareVersion(string $version1, string $version2): int {
        $first = array_map("intval", explode(".", $version1));
        $second = array_map("intval", explode(".", $version2));
        $length = max(count($first), count($second));
        for ($i = 0; $i < $length; $i++) {
            $a = $first[$i] ?? 0;
            $b = $second[$i] ?? 0;
            if ($a !== $b) return $a < $b ? -1 : 1;
        }
        return 0;
    }
}