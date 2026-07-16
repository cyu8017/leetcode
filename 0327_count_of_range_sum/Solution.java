// LeetCode 0327 - Count of Range Sum

// https://leetcode.com/problems/count-of-range-sum/



class Solution {

    private long[] prefix;

    private long[] temp;



    public int countRangeSum(int[] nums, int lower, int upper) {

        prefix = new long[nums.length + 1];

        temp = new long[prefix.length];

        for (int index = 0; index < nums.length; index++) {

            prefix[index + 1] = prefix[index] + nums[index];

        }

        return mergeSort(0, prefix.length - 1, lower, upper);

    }



    private int mergeSort(int left, int right, int lower, int upper) {

        if (left >= right) {

            return 0;

        }

        int mid = (left + right) / 2;

        int count = mergeSort(left, mid, lower, upper) + mergeSort(mid + 1, right, lower, upper);

        int start = mid + 1;

        int end = mid + 1;

        for (int index = left; index <= mid; index++) {

            while (start <= right && prefix[start] - prefix[index] < lower) {

                start++;

            }

            while (end <= right && prefix[end] - prefix[index] <= upper) {

                end++;

            }

            count += end - start;

        }

        int tempLeft = left;

        int tempRight = mid + 1;

        int write = left;

        while (tempLeft <= mid && tempRight <= right) {

            if (prefix[tempLeft] <= prefix[tempRight]) {

                temp[write++] = prefix[tempLeft++];

            } else {

                temp[write++] = prefix[tempRight++];

            }

        }

        while (tempLeft <= mid) {

            temp[write++] = prefix[tempLeft++];

        }

        while (tempRight <= right) {

            temp[write++] = prefix[tempRight++];

        }

        for (int index = left; index <= right; index++) {

            prefix[index] = temp[index];

        }

        return count;

    }

}

