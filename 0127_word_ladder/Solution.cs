// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

using System.Collections.Generic;

public class Solution {
    public int LadderLength(string beginWord, string endWord, IList<string> wordList) {
        var words = new HashSet<string>(wordList);
        if (!words.Contains(endWord)) return 0;

        var queue = new Queue<string>();
        var visited = new HashSet<string> { beginWord };
        queue.Enqueue(beginWord);
        int steps = 1;
        while (queue.Count > 0) {
            int size = queue.Count;
            while (size-- > 0) {
                string word = queue.Dequeue();
                if (word == endWord) return steps;
                char[] chars = word.ToCharArray();
                for (int i = 0; i < chars.Length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        string next = new string(chars);
                        if (words.Contains(next) && visited.Add(next)) queue.Enqueue(next);
                    }
                    chars[i] = original;
                }
            }
            steps++;
        }
        return 0;
    }
}