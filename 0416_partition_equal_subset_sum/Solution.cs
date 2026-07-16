// LeetCode 0416 - Partition Equal Subset Sum

// https://leetcode.com/problems/partition-equal-subset-sum/



public class Solution {

    public bool CanPartition(int[] nums) {

        int total = nums.Sum();



        if (total % 2 != 0) {

            return false;

        }



        int target = total / 2;

        HashSet<int> possible = new() { 0 };



        foreach (int value in nums) {

            HashSet<int> next = new();



            foreach (int amount in possible) {

                int sum = amount + value;



                if (sum <= target) {

                    next.Add(sum);

                }

            }



            possible.UnionWith(next);



            if (possible.Contains(target)) {

                return true;

            }

        }



        return possible.Contains(target);

    }

}
