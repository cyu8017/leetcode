// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

using System.Collections.Generic;

public class WordDistance {
    private readonly Dictionary<string, List<int>> positions = new();

    public WordDistance(string[] wordsDict) {
        for (int index = 0; index < wordsDict.Length; index++) {
            if (!positions.TryGetValue(wordsDict[index], out List<int>? list)) {
                list = new List<int>();
                positions[wordsDict[index]] = list;
            }
            list.Add(index);
        }
    }

    public int Shortest(string word1, string word2) {
        List<int> left = positions[word1];
        List<int> right = positions[word2];
        int i = 0;
        int j = 0;
        int best = int.MaxValue;
        while (i < left.Count && j < right.Count) {
            best = System.Math.Min(best, System.Math.Abs(left[i] - right[j]));
            if (left[i] <= right[j]) {
                i++;
            } else {
                j++;
            }
        }
        return best;
    }
}
