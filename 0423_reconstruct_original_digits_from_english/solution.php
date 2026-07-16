// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function originalDigits($s) {
        return $this->original_digits($s);
    }

    /**
     * @param String $s
     * @return String
     */
    function original_digits($s) {
        $counts = array_count_values(str_split($s));
        $digitCounts = array_fill(0, 10, 0);
        $digitCounts[0] = $counts['z'] ?? 0;
        $digitCounts[2] = $counts['w'] ?? 0;
        $digitCounts[4] = $counts['u'] ?? 0;
        $digitCounts[6] = $counts['x'] ?? 0;
        $digitCounts[8] = $counts['g'] ?? 0;
        $digitCounts[1] = ($counts['o'] ?? 0) - $digitCounts[0] - $digitCounts[2] - $digitCounts[4];
        $digitCounts[3] = ($counts['h'] ?? 0) - $digitCounts[8];
        $digitCounts[5] = ($counts['f'] ?? 0) - $digitCounts[4];
        $digitCounts[7] = ($counts['s'] ?? 0) - $digitCounts[6];
        $digitCounts[9] = ($counts['i'] ?? 0) - $digitCounts[5] - $digitCounts[6] - $digitCounts[8];

        $result = '';
        for ($digit = 0; $digit < 10; $digit++) {
            $result .= str_repeat((string)$digit, $digitCounts[$digit]);
        }
        return $result;
    }
}
