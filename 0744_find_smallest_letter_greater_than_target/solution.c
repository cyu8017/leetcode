// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int left = 0, right = lettersSize;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return letters[left % lettersSize];
}
