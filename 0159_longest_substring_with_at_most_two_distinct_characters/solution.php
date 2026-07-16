// LeetCode 0159 - Longest Substring with At Most Two Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution {
    function lengthOfLongestSubstringTwoDistinct(string $s): int {
        $characters = preg_split('//u', $s, -1, PREG_SPLIT_NO_EMPTY);
        $counts = [];
        $left = 0;
        $best = 0;
        foreach ($characters as $right => $character) {
            $counts[$character] = ($counts[$character] ?? 0) + 1;
            while (count($counts) > 2) {
                $leftCharacter = $characters[$left];
                $counts[$leftCharacter]--;
                if ($counts[$leftCharacter] === 0) {
                    unset($counts[$leftCharacter]);
                }
                $left++;
            }
            $best = max($best, $right - $left + 1);
        }
        return $best;
    }
}