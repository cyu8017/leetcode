// LeetCode 0411 - Minimum Unique Word Abbreviation

// https://leetcode.com/problems/minimum-unique-word-abbreviation/



import java.util.ArrayList;

import java.util.List;



class Solution {

    private String target;

    private List<String> words;

    private int bestLen;

    private String result;



    public String minAbbreviation(String target, List<String> dictionary) {

        this.target = target;

        this.words = new ArrayList<>();



        for (String word : dictionary) {

            if (word.length() == target.length()) {

                this.words.add(word);

            }

        }



        bestLen = target.length() + 1;

        result = target;

        dfs(0, new ArrayList<>(), 0);

        return result;

    }



    private boolean matches(String word, String abbr) {

        int index = 0;

        int pointer = 0;



        while (index < word.length() && pointer < abbr.length()) {

            if (Character.isDigit(abbr.charAt(pointer))) {

                if (abbr.charAt(pointer) == '0') {

                    return false;

                }



                int number = 0;



                while (pointer < abbr.length() && Character.isDigit(abbr.charAt(pointer))) {

                    number = number * 10 + (abbr.charAt(pointer) - '0');

                    pointer++;

                }



                index += number;

            } else {

                if (word.charAt(index) != abbr.charAt(pointer)) {

                    return false;

                }



                index++;

                pointer++;

            }

        }



        return index == word.length() && pointer == abbr.length();

    }



    private boolean valid(String abbr) {

        if (!matches(target, abbr)) {

            return false;

        }



        for (String word : words) {

            if (matches(word, abbr)) {

                return false;

            }

        }



        return true;

    }



    private void dfs(int index, List<String> parts, int skip) {

        if (index == target.length()) {

            StringBuilder builder = new StringBuilder();



            for (String part : parts) {

                builder.append(part);

            }



            if (skip != 0) {

                builder.append(skip);

            }



            String abbr = builder.toString();



            if (valid(abbr)) {

                if (abbr.length() < bestLen || (abbr.length() == bestLen && abbr.compareTo(result) < 0)) {

                    bestLen = abbr.length();

                    result = abbr;

                }

            }



            return;

        }



        dfs(index + 1, parts, skip + 1);



        List<String> newParts = new ArrayList<>(parts);



        if (skip != 0) {

            newParts.add(String.valueOf(skip));

        }



        newParts.add(String.valueOf(target.charAt(index)));

        dfs(index + 1, newParts, 0);

    }

}
