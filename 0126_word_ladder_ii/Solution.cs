// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> FindLadders(string beginWord, string endWord, IList<string> wordList) {
        var words = new HashSet<string>(wordList);
        var result = new List<IList<string>>();
        if (!words.Contains(endWord)) return result;

        var parents = new Dictionary<string, List<string>>();
        var visited = new HashSet<string> { beginWord };
        var queue = new Queue<string>();
        queue.Enqueue(beginWord);
        bool found = false;

        while (queue.Count > 0 && !found) {
            var levelVisited = new HashSet<string>();
            int size = queue.Count;
            while (size-- > 0) {
                string word = queue.Dequeue();
                char[] chars = word.ToCharArray();
                for (int i = 0; i < chars.Length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        string next = new string(chars);
                        if (!words.Contains(next) || visited.Contains(next)) continue;
                        if (levelVisited.Add(next)) queue.Enqueue(next);
                        if (!parents.ContainsKey(next)) parents[next] = new List<string>();
                        parents[next].Add(word);
                        if (next == endWord) found = true;
                    }
                    chars[i] = original;
                }
            }
            visited.UnionWith(levelVisited);
        }

        if (found) BuildPaths(endWord, beginWord, parents, new List<string>(), result);
        return result;
    }

    private void BuildPaths(string word, string beginWord, Dictionary<string, List<string>> parents,
                            List<string> path, IList<IList<string>> result) {
        path.Add(word);
        if (word == beginWord) {
            var ladder = new List<string>(path);
            ladder.Reverse();
            result.Add(ladder);
        } else if (parents.TryGetValue(word, out var previous)) {
            foreach (string parent in previous) BuildPaths(parent, beginWord, parents, path, result);
        }
        path.RemoveAt(path.Count - 1);
    }
}