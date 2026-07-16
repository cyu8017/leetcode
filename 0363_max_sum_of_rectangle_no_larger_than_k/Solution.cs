// LeetCode 0363 - Max Sum of Rectangle No Larger Than K

// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/



public class Solution {

    public int MaxSumSubmatrix(int[][] matrix, int k) {

        int rows = matrix.Length;

        int cols = rows == 0 ? 0 : matrix[0].Length;

        int result = int.MinValue;



        for (int top = 0; top < rows; top++) {

            int[] colSums = new int[cols];

            for (int bottom = top; bottom < rows; bottom++) {

                List<long> prefixSums = new() { 0L };

                long running = 0;



                for (int col = 0; col < cols; col++) {

                    colSums[col] += matrix[bottom][col];

                    running += colSums[col];

                    int index = BisectLeft(prefixSums, running - k);

                    if (index < prefixSums.Count) {

                        result = Math.Max(result, (int)(running - prefixSums[index]));

                    }

                    Insort(prefixSums, running);

                }

            }

        }



        return result;

    }



    private static int BisectLeft(List<long> list, long value) {

        int left = 0;

        int right = list.Count;

        while (left < right) {

            int mid = left + (right - left) / 2;

            if (list[mid] < value) {

                left = mid + 1;

            } else {

                right = mid;

            }

        }

        return left;

    }



    private static void Insort(List<long> list, long value) {

        list.Insert(BisectLeft(list, value), value);

    }

}
