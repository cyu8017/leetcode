// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        $last = [];
        $best = 0;
        $start = 0;
        $n = strlen($s);

        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (array_key_exists($ch, $last) && $last[$ch] >= $start) {
                $start = $last[$ch] + 1;
            }
            $last[$ch] = $i;
            $best = max($best, $i - $start + 1);
        }

        return $best;
    }
}
