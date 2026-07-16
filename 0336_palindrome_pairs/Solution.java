// LeetCode 0336 - Palindrome Pairs

// https://leetcode.com/problems/palindrome-pairs/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.HashSet;

import java.util.List;

import java.util.Map;

import java.util.Set;



class Solution {

    public List<List<Integer>> palindromePairs(String[] words) {

        Map<String, Integer> wordMap = new HashMap<>();

        for (int index = 0; index < words.length; index++) {

            wordMap.put(words[index], index);

        }



        Set<String> result = new HashSet<>();

        for (int index = 0; index < words.length; index++) {

            String word = words[index];

            for (int split = 0; split <= word.length(); split++) {

                String left = word.substring(0, split);

                String right = word.substring(split);

                if (isPalindrome(left)) {

                    String reversedRight = new StringBuilder(right).reverse().toString();

                    Integer otherIndex = wordMap.get(reversedRight);

                    if (otherIndex != null && otherIndex != index) {

                        result.add(otherIndex + "," + index);

                    }

                }

                if (isPalindrome(right)) {

                    String reversedLeft = new StringBuilder(left).reverse().toString();

                    Integer otherIndex = wordMap.get(reversedLeft);

                    if (otherIndex != null && otherIndex != index) {

                        result.add(index + "," + otherIndex);

                    }

                }

            }

        }



        List<List<Integer>> pairs = new ArrayList<>();

        for (String pair : result) {

            String[] parts = pair.split(",");

            List<Integer> entry = new ArrayList<>();

            entry.add(Integer.parseInt(parts[0]));

            entry.add(Integer.parseInt(parts[1]));

            pairs.add(entry);

        }

        return pairs;

    }



    private boolean isPalindrome(String value) {

        int left = 0;

        int right = value.length() - 1;

        while (left < right) {

            if (value.charAt(left) != value.charAt(right)) {

                return false;

            }

            left++;

            right--;

        }

        return true;

    }

}
