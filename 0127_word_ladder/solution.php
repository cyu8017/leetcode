// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

class Solution {
    /**
     * @param String $beginWord
     * @param String $endWord
     * @param String[] $wordList
     * @return Integer
     */
    function ladderLength($beginWord, $endWord, $wordList) {
        $words = array_fill_keys($wordList, true);
        if (!isset($words[$endWord])) {
            return 0;
        }

        $queue = [[$beginWord, 1]];
        $head = 0;
        $visited = [$beginWord => true];
        while ($head < count($queue)) {
            [$word, $steps] = $queue[$head++];
            if ($word === $endWord) {
                return $steps;
            }
            $characters = str_split($word);
            for ($index = 0; $index < count($characters); $index++) {
                $original = $characters[$index];
                for ($code = ord('a'); $code <= ord('z'); $code++) {
                    $characters[$index] = chr($code);
                    $next = implode('', $characters);
                    if (isset($words[$next]) && !isset($visited[$next])) {
                        $visited[$next] = true;
                        $queue[] = [$next, $steps + 1];
                    }
                }
                $characters[$index] = $original;
            }
        }
        return 0;
    }
}