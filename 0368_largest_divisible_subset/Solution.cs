// LeetCode 0368 - Largest Divisible Subset

// https://leetcode.com/problems/largest-divisible-subset/



using System.Collections.Generic;



public class Solution {

    public IList<int> LargestDivisibleSubset(int[] nums) {

        Array.Sort(nums);

        Dictionary<int, List<int>> chains = new();

        foreach (int num in nums) {

            chains[num] = new List<int> { num };

        }



        List<int> best = new();

        foreach (int num in nums) {

            foreach (int prev in chains.Keys) {

                if (prev < num && num % prev == 0 && chains[prev].Count + 1 > chains[num].Count) {

                    chains[num] = new List<int>(chains[prev]) { num };

                }

            }

            if (chains[num].Count > best.Count) {

                best = chains[num];

            }

        }



        return best;

    }

}
