// LeetCode 0387 - First Unique Character in a String

// https://leetcode.com/problems/first-unique-character-in-a-string/



public class Solution {

    public int FirstUniqChar(string s) {

        Dictionary<char, int> counts = new();

        foreach (char ch in s) {

            counts.TryGetValue(ch, out int count);

            counts[ch] = count + 1;

        }



        for (int index = 0; index < s.Length; index++) {

            if (counts[s[index]] == 1) {

                return index;

            }

        }

        return -1;

    }

}
