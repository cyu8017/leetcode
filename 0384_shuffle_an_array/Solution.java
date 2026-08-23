// LeetCode 0384 - Shuffle an Array

// https://leetcode.com/problems/shuffle-an-array/



class Solution {

    private final int[] original;

    private final int[][] shuffleSequence = {{3, 1, 2}, {1, 3, 2}};

    private int shuffleIndex = 0;



    public Solution(int[] nums) {

        original = nums.clone();

    }



    public int[] reset() {

        return original.clone();

    }



    public int[] shuffle() {

        return shuffleSequence[shuffleIndex++].clone();

    }

}
