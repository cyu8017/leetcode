// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

class Solution {
    /**
     * @param String $beginWord
     * @param String $endWord
     * @param String[] $wordList
     * @return String[][]
     */
    function findLadders($beginWord, $endWord, $wordList) {
        $words = array_fill_keys($wordList, true);
        if (!isset($words[$endWord])) {
            return [];
        }

        $parents = [];
        $visited = [$beginWord => true];
        $queue = [$beginWord];
        $found = false;
        while (!empty($queue) && !$found) {
            $levelVisited = [];
            $nextQueue = [];
            foreach ($queue as $word) {
                $characters = str_split($word);
                for ($index = 0; $index < count($characters); $index++) {
                    $original = $characters[$index];
                    for ($code = ord('a'); $code <= ord('z'); $code++) {
                        $characters[$index] = chr($code);
                        $next = implode('', $characters);
                        if (!isset($words[$next]) || isset($visited[$next])) {
                            continue;
                        }
                        if (!isset($levelVisited[$next])) {
                            $levelVisited[$next] = true;
                            $nextQueue[] = $next;
                        }
                        $parents[$next][] = $word;
                        if ($next === $endWord) {
                            $found = true;
                        }
                    }
                    $characters[$index] = $original;
                }
            }
            $visited += $levelVisited;
            $queue = $nextQueue;
        }
        if (!$found) {
            return [];
        }

        $results = [];
        $build = function ($word, $path) use (&$build, &$results, &$parents, $beginWord) {
            if ($word === $beginWord) {
                $results[] = array_reverse($path);
                return;
            }
            foreach ($parents[$word] as $parent) {
                $path[] = $parent;
                $build($parent, $path);
                array_pop($path);
            }
        };
        $build($endWord, [$endWord]);
        sort($results);
        return $results;
    }
}