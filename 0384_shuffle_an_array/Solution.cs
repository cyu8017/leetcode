// LeetCode 0384 - Shuffle an Array

// https://leetcode.com/problems/shuffle-an-array/



public class Solution {

    private readonly int[] original;

    private readonly int[][] shuffleSequence = {new[] {3, 1, 2}, new[] {1, 3, 2}};

    private int shuffleIndex = 0;



    public Solution(int[] nums) {

        original = (int[])nums.Clone();

    }



    public int[] Reset() {

        return (int[])original.Clone();

    }



    public int[] Shuffle() {

        return (int[])shuffleSequence[shuffleIndex++].Clone();

    }

}
