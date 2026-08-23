// LeetCode 0403 - Frog Jump

// https://leetcode.com/problems/frog-jump/



using System.Collections.Generic;



public class Solution {

    public bool CanCross(int[] stones) {

        HashSet<int> stoneSet = new(stones);

        Dictionary<int, HashSet<int>> jumps = new();



        foreach (int stone in stones) {

            jumps[stone] = new HashSet<int>();

        }

        jumps[0].Add(0);



        foreach (int stone in stones) {

            foreach (int jump in jumps[stone]) {

                foreach (int nextJump in new[] { jump - 1, jump, jump + 1 }) {

                    if (nextJump > 0) {

                        int nextStone = stone + nextJump;

                        if (stoneSet.Contains(nextStone)) {

                            jumps[nextStone].Add(nextJump);

                        }

                    }

                }

            }

        }



        return jumps[stones[^1]].Count > 0;

    }

}
