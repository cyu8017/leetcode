// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

int maxChunksToSorted(int* arr, int arrSize) {
    int chunks = 0, maxSoFar = 0;
    for (int i = 0; i < arrSize; i++) {
        if (arr[i] > maxSoFar) maxSoFar = arr[i];
        if (maxSoFar == i) chunks++;
    }
    return chunks;
}
