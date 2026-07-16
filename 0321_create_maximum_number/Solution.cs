// LeetCode 0321 - Create Maximum Number

// https://leetcode.com/problems/create-maximum-number/



using System.Collections.Generic;



public class Solution {

    public int[] MaxNumber(int[] nums1, int[] nums2, int k) {

        int[] best = System.Array.Empty<int>();

        int minFirst = System.Math.Max(0, k - nums2.Length);

        int maxFirst = System.Math.Min(k, nums1.Length);

        for (int takeFirst = minFirst; takeFirst <= maxFirst; takeFirst++) {

            int takeSecond = k - takeFirst;

            int[] candidate = Merge(PickMax(nums1, takeFirst), PickMax(nums2, takeSecond));

            if (Compare(candidate, best) > 0) {

                best = candidate;

            }

        }

        return best;

    }



    private int[] PickMax(int[] values, int count) {

        int drop = values.Length - count;

        List<int> stack = new();

        foreach (int value in values) {

            while (drop > 0 && stack.Count > 0 && stack[^1] < value) {

                stack.RemoveAt(stack.Count - 1);

                drop--;

            }

            stack.Add(value);

        }

        return stack.GetRange(0, count).ToArray();

    }



    private int[] Merge(int[] first, int[] second) {

        int[] result = new int[first.Length + second.Length];

        int left = 0;

        int right = 0;

        int write = 0;

        while (left < first.Length && right < second.Length) {

            if (CompareSuffix(first, left, second, right) > 0) {

                result[write++] = first[left++];

            } else {

                result[write++] = second[right++];

            }

        }

        while (left < first.Length) {

            result[write++] = first[left++];

        }

        while (right < second.Length) {

            result[write++] = second[right++];

        }

        return result;

    }



    private int CompareSuffix(int[] first, int left, int[] second, int right) {

        for (int index = left, other = right; index < first.Length && other < second.Length; index++, other++) {

            if (first[index] != second[other]) {

                return first[index].CompareTo(second[other]);

            }

        }

        return (first.Length - left).CompareTo(second.Length - right);

    }



    private int Compare(int[] left, int[] right) {

        if (left.Length != right.Length) {

            return left.Length.CompareTo(right.Length);

        }

        for (int index = 0; index < left.Length; index++) {

            if (left[index] != right[index]) {

                return left[index].CompareTo(right[index]);

            }

        }

        return 0;

    }

}

