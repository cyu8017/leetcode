// LeetCode 0387 - First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function firstUniqChar($s) {
        return $this->first_uniq_char($s);
    }

    /**
     * @param String $s
     * @return Integer
     */
    function first_uniq_char($s) {
        $counts = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $char = $s[$index];
            $counts[$char] = ($counts[$char] ?? 0) + 1;
        }

        for ($index = 0; $index < $length; $index++) {
            if ($counts[$s[$index]] === 1) {
                return $index;
            }
        }

        return -1;
    }
}
