// LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

int countTriplets(int* arr, int arrSize) {
    int answer = 0;
    for (int i = 0; i < arrSize; i++) {
        int value = 0;
        for (int k = i; k < arrSize; k++) {
            value ^= arr[k];
            if (value == 0) answer += k - i;
        }
    }
    return answer;
}
