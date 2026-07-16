// LeetCode 0354 - Russian Doll Envelopes

// https://leetcode.com/problems/russian-doll-envelopes/



using System.Collections.Generic;



public class Solution {

    public int MaxEnvelopes(int[][] envelopes) {

        Array.Sort(envelopes, (left, right) => {

            if (left[0] != right[0]) {

                return left[0].CompareTo(right[0]);

            }

            return right[1].CompareTo(left[1]);

        });



        List<int> tails = new();

        foreach (int[] envelope in envelopes) {

            int height = envelope[1];

            int index = LowerBound(tails, height);

            if (index == tails.Count) {

                tails.Add(height);

            } else {

                tails[index] = height;

            }

        }



        return tails.Count;

    }



    private int LowerBound(List<int> values, int target) {

        int left = 0;

        int right = values.Count;

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (values[mid] < target) {

                left = mid + 1;

            } else {

                right = mid;

            }

        }

        return left;

    }

}
