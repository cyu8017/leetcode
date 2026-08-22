// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize - 1;
    int best = 0;

    while (left < right) {
        int width = right - left;
        int h = height[left] < height[right] ? height[left] : height[right];
        if (h * width > best) {
            best = h * width;
        }
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return best;
}
