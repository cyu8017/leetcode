// LeetCode 0363 - Max Sum of Rectangle No Larger Than K

// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/



import java.util.ArrayList;

import java.util.List;



class Solution {

    public int maxSumSubmatrix(int[][] matrix, int k) {

        int rows = matrix.length;

        int cols = rows == 0 ? 0 : matrix[0].length;

        int result = Integer.MIN_VALUE;



        for (int top = 0; top < rows; top++) {

            int[] colSums = new int[cols];

            for (int bottom = top; bottom < rows; bottom++) {

                List<Long> prefixSums = new ArrayList<>();

                prefixSums.add(0L);

                long running = 0;



                for (int col = 0; col < cols; col++) {

                    colSums[col] += matrix[bottom][col];

                    running += colSums[col];

                    int index = bisectLeft(prefixSums, running - k);

                    if (index < prefixSums.size()) {

                        result = Math.max(result, (int) (running - prefixSums.get(index)));

                    }

                    insort(prefixSums, running);

                }

            }

        }



        return result;

    }



    private int bisectLeft(List<Long> list, long value) {

        int left = 0;

        int right = list.size();

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (list.get(mid) < value) {

                left = mid + 1;

            } else {

                right = mid;

            }

        }

        return left;

    }



    private void insort(List<Long> list, long value) {

        list.add(bisectLeft(list, value), value);

    }

}
