// LeetCode 0383 - Ransom Note

// https://leetcode.com/problems/ransom-note/



public class Solution {

    public bool CanConstruct(string ransomNote, string magazine) {

        Dictionary<char, int> counts = new();

        foreach (char ch in magazine) {

            counts.TryGetValue(ch, out int count);

            counts[ch] = count + 1;

        }



        foreach (char ch in ransomNote) {

            if (!counts.TryGetValue(ch, out int remaining) || remaining == 0) {

                return false;

            }

            counts[ch] = remaining - 1;

        }

        return true;

    }

}
