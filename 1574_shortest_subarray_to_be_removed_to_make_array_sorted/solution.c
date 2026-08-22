// LeetCode 1574 - Shortest Subarray to be Removed to Make Array Sorted
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

int findLengthOfShortestSubarray(int* arr, int arrSize) {
    int n = arrSize;
    int right = n - 1;
    while (right && arr[right - 1] <= arr[right]) right--;
    if (right == 0) return 0;
    int answer = right, left = 0;
    while (1) {
        while (right < n && arr[right] < arr[left]) right++;
        if (right - left - 1 < answer) answer = right - left - 1;
        left++;
        if (left >= n || (left > 0 && arr[left - 1] > arr[left])) break;
    }
    return answer;
}
