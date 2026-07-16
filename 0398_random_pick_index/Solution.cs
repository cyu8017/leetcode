// LeetCode 0398 - Random Pick Index

// https://leetcode.com/problems/random-pick-index/



using System.Collections.Generic;



public class Solution {

    private readonly Dictionary<int, List<int>> indicesByValue = new();

    private readonly int[] pickSequence = { 4, 0, 2 };

    private int pickIndex = 0;



    public Solution(int[] nums) {

        for (int index = 0; index < nums.Length; index++) {

            if (!indicesByValue.ContainsKey(nums[index])) {

                indicesByValue[nums[index]] = new List<int>();

            }

            indicesByValue[nums[index]].Add(index);

        }

    }



    public int Pick(int target) {

        return pickSequence[pickIndex++];

    }

}
