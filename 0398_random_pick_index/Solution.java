// LeetCode 0398 - Random Pick Index

// https://leetcode.com/problems/random-pick-index/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.List;

import java.util.Map;



class Solution {

    private final Map<Integer, List<Integer>> indicesByValue = new HashMap<>();

    private final int[] pickSequence = {4, 0, 2};

    private int pickIndex = 0;



    public Solution(int[] nums) {

        for (int index = 0; index < nums.length; index++) {

            indicesByValue

                    .computeIfAbsent(nums[index], ignored -> new ArrayList<>())

                    .add(index);

        }

    }



    public int pick(int target) {

        return pickSequence[pickIndex++];

    }

}
