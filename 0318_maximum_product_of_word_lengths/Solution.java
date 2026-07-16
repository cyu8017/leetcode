// LeetCode 0318 - Maximum Product of Word Lengths

// https://leetcode.com/problems/maximum-product-of-word-lengths/



class Solution {

    public int maxProduct(String[] words) {

        int count = words.length;

        int[] masks = new int[count];

        int[] lengths = new int[count];

        for (int index = 0; index < count; index++) {

            String word = words[index];

            int mask = 0;

            boolean valid = true;

            for (int charIndex = 0; charIndex < word.length(); charIndex++) {

                int bit = 1 << (word.charAt(charIndex) - 'a');

                if ((mask & bit) != 0) {

                    valid = false;

                    break;

                }

                mask |= bit;

            }

            masks[index] = valid ? mask : 0;

            lengths[index] = word.length();

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

                    best = Math.max(best, lengths[left] * lengths[right]);

                }

            }

        }

        return best;

    }

}

