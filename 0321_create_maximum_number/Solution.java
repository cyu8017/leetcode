// LeetCode 0321 - Create Maximum Number

// https://leetcode.com/problems/create-maximum-number/



import java.util.ArrayList;

import java.util.List;



class Solution {

    public int[] maxNumber(int[] nums1, int[] nums2, int k) {

        int[] best = new int[0];

        int minFirst = Math.max(0, k - nums2.length);

        int maxFirst = Math.min(k, nums1.length);

        for (int takeFirst = minFirst; takeFirst <= maxFirst; takeFirst++) {

            int takeSecond = k - takeFirst;

            int[] candidate = merge(pickMax(nums1, takeFirst), pickMax(nums2, takeSecond));

            if (compare(candidate, best) > 0) {

                best = candidate;

            }

        }

        return best;

    }



    private int[] pickMax(int[] values, int count) {

        int drop = values.length - count;

        List<Integer> stack = new ArrayList<>();

        for (int value : values) {

            while (drop > 0 && !stack.isEmpty() && stack.get(stack.size() - 1) < value) {

                stack.remove(stack.size() - 1);

                drop--;

            }

            stack.add(value);

        }

        int[] result = new int[count];

        for (int index = 0; index < count; index++) {

            result[index] = stack.get(index);

        }

        return result;

    }



    private int[] merge(int[] first, int[] second) {

        int[] result = new int[first.length + second.length];

        int left = 0;

        int right = 0;

        int write = 0;

        while (left < first.length && right < second.length) {

            if (compareSuffix(first, left, second, right) > 0) {

                result[write++] = first[left++];

            } else {

                result[write++] = second[right++];

            }

        }

        while (left < first.length) {

            result[write++] = first[left++];

        }

        while (right < second.length) {

            result[write++] = second[right++];

        }

        return result;

    }



    private int compareSuffix(int[] first, int left, int[] second, int right) {

        for (int index = left, other = right; index < first.length && other < second.length; index++, other++) {

            if (first[index] != second[other]) {

                return Integer.compare(first[index], second[other]);

            }

        }

        return Integer.compare(first.length - left, second.length - right);

    }



    private int compare(int[] left, int[] right) {

        if (left.length != right.length) {

            return Integer.compare(left.length, right.length);

        }

        for (int index = 0; index < left.length; index++) {

            if (left[index] != right[index]) {

                return Integer.compare(left[index], right[index]);

            }

        }

        return 0;

    }

}

