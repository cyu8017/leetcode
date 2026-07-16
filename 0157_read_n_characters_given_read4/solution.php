// LeetCode 0157 - Read N Characters Given Read4
// https://leetcode.com/problems/read-n-characters-given-read4/

class Solution {
    function read(string $file, int $n): int {
        $fileIndex = 0;
        $copied = 0;
        while ($copied < $n && $fileIndex < strlen($file)) {
            $count = min(4, strlen($file) - $fileIndex);
            $fileIndex += $count;
            $copied += min($count, $n - $copied);
        }
        return $copied;
    }
}