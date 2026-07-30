// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

using System.Collections.Generic;
using System.Linq;

public class CombinationIterator {
    private readonly string[] items;
    private int index = 0;

    public CombinationIterator(string characters, int combinationLength) {
        items = BuildCombinations(characters, combinationLength);
    }

    public string Next() {
        return items[index++];
    }

    public bool HasNext() {
        return index < items.Length;
    }

    private static string[] BuildCombinations(string characters, int k) {
        var result = new List<string>();
        void Dfs(int start, char[] path, int depth) {
            if (depth == k) {
                result.Add(new string(path, 0, k));
                return;
            }
            for (int i = start; i < characters.Length; i++) {
                path[depth] = characters[i];
                Dfs(i + 1, path, depth + 1);
            }
        }
        Dfs(0, new char[k], 0);
        return result.ToArray();
    }
}
