// LeetCode 0354 - Russian Doll Envelopes

// https://leetcode.com/problems/russian-doll-envelopes/



import java.util.ArrayList;

import java.util.Arrays;

import java.util.Comparator;

import java.util.List;



class Solution {

    public int maxEnvelopes(int[][] envelopes) {

        Arrays.sort(envelopes, Comparator

            .comparingInt((int[] item) -> item[0])

            .thenComparingInt(item -> -item[1]));



        List<Integer> tails = new ArrayList<>();

        for (int[] envelope : envelopes) {

            int height = envelope[1];

            int index = lowerBound(tails, height);

            if (index == tails.size()) {

                tails.add(height);

            } else {

                tails.set(index, height);

            }

        }



        return tails.size();

    }



    private int lowerBound(List<Integer> values, int target) {

        int left = 0;

        int right = values.size();

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (values.get(mid) < target) {

                left = mid + 1;

            } else {

                right = mid;

            }

        }

        return left;

    }

}
