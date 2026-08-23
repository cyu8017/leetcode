// LeetCode 0416 - Partition Equal Subset Sum

// https://leetcode.com/problems/partition-equal-subset-sum/



import java.util.HashSet;

import java.util.Set;



class Solution {

    public boolean canPartition(int[] nums) {

        int total = 0;



        for (int value : nums) {

            total += value;

        }



        if (total % 2 != 0) {

            return false;

        }



        int target = total / 2;

        Set<Integer> possible = new HashSet<>();

        possible.add(0);



        for (int value : nums) {

            Set<Integer> next = new HashSet<>();



            for (int amount : possible) {

                int sum = amount + value;



                if (sum <= target) {

                    next.add(sum);

                }

            }



            possible.addAll(next);



            if (possible.contains(target)) {

                return true;

            }

        }



        return possible.contains(target);

    }

}
