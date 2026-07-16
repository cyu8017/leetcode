// LeetCode 0318 - Maximum Product of Word Lengths

// https://leetcode.com/problems/maximum-product-of-word-lengths/



public class Solution {

    public int MaxProduct(string[] words) {

        int count = words.Length;

        int[] masks = new int[count];

        int[] lengths = new int[count];

        for (int index = 0; index < count; index++) {

            string word = words[index];

            int mask = 0;

            bool valid = true;

            for (int charIndex = 0; charIndex < word.Length; charIndex++) {

                int bit = 1 << (word[charIndex] - 'a');

                if ((mask & bit) != 0) {

                    valid = false;

                    break;

                }

                mask |= bit;

            }

            masks[index] = valid ? mask : 0;

            lengths[index] = word.Length;

        }



        int best = 0;

        for (int left = 0; left < count; left++) {

            if (masks[left] == 0) {

                continue;

            }

            for (int right = left + 1; right < count; right++) {

                if (masks[right] == 0) {

                    continue;

                }

                if ((masks[left] & masks[right]) == 0) {

                    best = System.Math.Max(best, lengths[left] * lengths[right]);

                }

            }

        }

        return best;

    }

}

