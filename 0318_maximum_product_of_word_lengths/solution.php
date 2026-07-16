// LeetCode 0318 - Maximum Product of Word Lengths
// https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function maxProduct($words) {
        $masks = [];
        $lengths = [];
        foreach ($words as $word) {
            $mask = 0;
            $valid = true;
            $wordLength = strlen($word);
            for ($index = 0; $index < $wordLength; $index++) {
                $bit = 1 << (ord($word[$index]) - ord('a'));
                if ($mask & $bit) {
                    $valid = false;
                    break;
                }
                $mask |= $bit;
            }
            $masks[] = $valid ? $mask : 0;
            $lengths[] = $wordLength;
        }

        $best = 0;
        $count = count($words);
        for ($left = 0; $left < $count; $left++) {
            if ($masks[$left] === 0) {
                continue;
            }
            for ($right = $left + 1; $right < $count; $right++) {
                if ($masks[$right] === 0) {
                    continue;
                }
                if (($masks[$left] & $masks[$right]) === 0) {
                    $best = max($best, $lengths[$left] * $lengths[$right]);
                }
            }
        }
        return $best;
    }
}
