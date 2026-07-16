// LeetCode 0383 - Ransom Note
// https://leetcode.com/problems/ransom-note/

class Solution {
    /**
     * @param String $ransomNote
     * @param String $magazine
     * @return Boolean
     */
    function canConstruct($ransomNote, $magazine) {
        return $this->can_construct($ransomNote, $magazine);
    }

    /**
     * @param String $ransomNote
     * @param String $magazine
     * @return Boolean
     */
    function can_construct($ransomNote, $magazine) {
        $counts = [];
        $magazineLength = strlen($magazine);
        for ($index = 0; $index < $magazineLength; $index++) {
            $char = $magazine[$index];
            $counts[$char] = ($counts[$char] ?? 0) + 1;
        }

        $ransomLength = strlen($ransomNote);
        for ($index = 0; $index < $ransomLength; $index++) {
            $char = $ransomNote[$index];
            if (($counts[$char] ?? 0) === 0) {
                return false;
            }
            $counts[$char]--;
        }

        return true;
    }
}
