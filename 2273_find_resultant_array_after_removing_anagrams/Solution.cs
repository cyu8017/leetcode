// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

using System.Collections.Generic;

public class Solution {
    public IList<string> RemoveAnagrams(string[] words) {
        int[] Sig(string w) {
            int[] c = new int[26];
            foreach (char ch in w) c[ch - 'a']++;
            return c;
        }
        bool Eq(int[] a, int[] b) {
            for (int i = 0; i < 26; i++) if (a[i] != b[i]) return false;
            return true;
        }
        var ans = new List<string> { words[0] };
        int[] prev = Sig(words[0]);
        for (int i = 1; i < words.Length; i++) {
            int[] cur = Sig(words[i]);
            if (!Eq(cur, prev)) {
                ans.Add(words[i]);
                prev = cur;
            }
        }
        return ans;
    }
}
