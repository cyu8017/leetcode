// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution {
    /**
     * @param String $s
     * @param String[] $words
     * @return Integer[]
     */
    function findSubstring($s, $words) {
        if (empty($words) || $s === '') {
            return [];
        }

        $wordLen = strlen($words[0]);
        $wordCount = count($words);
        $need = array_count_values($words);
        $result = [];

        for ($start = 0; $start < $wordLen; $start++) {
            $left = $start;
            $counts = [];
            $used = 0;

            for ($right = $start; $right <= strlen($s) - $wordLen; $right += $wordLen) {
                $word = substr($s, $right, $wordLen);
                if (!isset($need[$word])) {
                    $counts = [];
                    $used = 0;
                    $left = $right + $wordLen;
                    continue;
                }

                if (!isset($counts[$word])) {
                    $counts[$word] = 0;
                }
                $counts[$word]++;
                $used++;

                while ($counts[$word] > $need[$word]) {
                    $leftWord = substr($s, $left, $wordLen);
                    $counts[$leftWord]--;
                    $used--;
                    $left += $wordLen;
                }

                if ($used === $wordCount) {
                    $result[] = $left;
                }
            }
        }

        sort($result);
        return $result;
    }
}
