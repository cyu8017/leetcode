// LeetCode 0336 - Palindrome Pairs

// https://leetcode.com/problems/palindrome-pairs/



using System.Collections.Generic;

using System.Linq;



public class Solution {

    public IList<IList<int>> PalindromePairs(string[] words) {

        Dictionary<string, int> wordMap = new();

        for (int index = 0; index < words.Length; index++) {

            wordMap[words[index]] = index;

        }



        HashSet<string> result = new();

        for (int index = 0; index < words.Length; index++) {

            string word = words[index];

            for (int split = 0; split <= word.Length; split++) {

                string left = word[..split];

                string right = word[split..];

                if (IsPalindrome(left)) {

                    string reversedRight = new string(right.Reverse().ToArray());

                    if (wordMap.TryGetValue(reversedRight, out int otherIndex) && otherIndex != index) {

                        result.Add($"{otherIndex},{index}");

                    }

                }

                if (IsPalindrome(right)) {

                    string reversedLeft = new string(left.Reverse().ToArray());

                    if (wordMap.TryGetValue(reversedLeft, out int otherIndex) && otherIndex != index) {

                        result.Add($"{index},{otherIndex}");

                    }

                }

            }

        }



        List<IList<int>> pairs = new();

        foreach (string pair in result) {

            string[] parts = pair.Split(',');

            pairs.Add(new List<int> { int.Parse(parts[0]), int.Parse(parts[1]) });

        }

        return pairs;

    }



    private static bool IsPalindrome(string value) {

        int left = 0;

        int right = value.Length - 1;

        while (left < right) {

            if (value[left] != value[right]) {

                return false;

            }

            left++;

            right--;

        }

        return true;

    }

}
