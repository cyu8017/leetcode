// LeetCode 0368 - Largest Divisible Subset

// https://leetcode.com/problems/largest-divisible-subset/



import java.util.ArrayList;

import java.util.Arrays;

import java.util.HashMap;

import java.util.List;

import java.util.Map;



class Solution {

    public List<Integer> largestDivisibleSubset(int[] nums) {

        Arrays.sort(nums);

        Map<Integer, List<Integer>> chains = new HashMap<>();

        for (int num : nums) {

            chains.put(num, new ArrayList<>(List.of(num)));

        }



        List<Integer> best = new ArrayList<>();

        for (int num : nums) {

            for (int prev : chains.keySet()) {

                if (prev < num && num % prev == 0 && chains.get(prev).size() + 1 > chains.get(num).size()) {

                    List<Integer> next = new ArrayList<>(chains.get(prev));

                    next.add(num);

                    chains.put(num, next);

                }

            }

            if (chains.get(num).size() > best.size()) {

                best = chains.get(num);

            }

        }



        return best;

    }

}
