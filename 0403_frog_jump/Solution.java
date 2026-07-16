// LeetCode 0403 - Frog Jump

// https://leetcode.com/problems/frog-jump/



import java.util.HashMap;

import java.util.HashSet;

import java.util.Map;

import java.util.Set;



class Solution {

    public boolean canCross(int[] stones) {

        Set<Integer> stoneSet = new HashSet<>();

        for (int stone : stones) {

            stoneSet.add(stone);

        }



        Map<Integer, Set<Integer>> jumps = new HashMap<>();

        for (int stone : stones) {

            jumps.put(stone, new HashSet<>());

        }

        jumps.get(0).add(0);



        for (int stone : stones) {

            for (int jump : jumps.get(stone)) {

                for (int nextJump : new int[] {jump - 1, jump, jump + 1}) {

                    if (nextJump > 0) {

                        int nextStone = stone + nextJump;

                        if (stoneSet.contains(nextStone)) {

                            jumps.get(nextStone).add(nextJump);

                        }

                    }

                }

            }

        }



        return !jumps.get(stones[stones.length - 1]).isEmpty();

    }

}
