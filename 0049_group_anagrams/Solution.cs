// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var groups = new Dictionary<string, List<string>>();

        foreach (var word in strs) {
            var chars = word.ToCharArray();
            Array.Sort(chars);
            var key = new string(chars);
            if (!groups.ContainsKey(key)) {
                groups[key] = new List<string>();
            }
            groups[key].Add(word);
        }

        var result = new List<IList<string>>();
        foreach (var group in groups.Values) {
            group.Sort();
            result.Add(group);
        }
        result.Sort((left, right) =>
            MinGroupIndex(strs, right).CompareTo(MinGroupIndex(strs, left)));
        return result;
    }

    private static int MinGroupIndex(string[] strs, IList<string> group) {
        var min = strs.Length;
        foreach (var word in group) {
            for (var i = 0; i < strs.Length; i++) {
                if (strs[i] == word) {
                    min = Math.Min(min, i);
                    break;
                }
            }
        }
        return min;
    }
}
