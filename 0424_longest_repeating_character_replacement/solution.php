// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function characterReplacement($s, $k) {
        return $this->character_replacement($s, $k);
    }

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function character_replacement($s, $k) {
        $counts = [];
        $left = 0;
        $best = 0;
        $maxCount = 0;
        $length = strlen($s);

        for ($right = 0; $right < $length; $right++) {
            $char = $s[$right];
            $counts[$char] = ($counts[$char] ?? 0) + 1;
            $maxCount = max($maxCount, $counts[$char]);
            while (($right - $left + 1) - $maxCount > $k) {
                $leftChar = $s[$left];
                $counts[$leftChar]--;
                $left++;
            }
            $best = max($best, $right - $left + 1);
        }

        return $best;
    }
}
