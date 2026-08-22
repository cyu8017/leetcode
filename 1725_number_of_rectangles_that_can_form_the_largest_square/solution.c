// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

int countGoodRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    int best = 0;
    int count = 0;
    for (int i = 0; i < rectanglesSize; i++) {
        int side = rectangles[i][0] < rectangles[i][1] ? rectangles[i][0] : rectangles[i][1];
        if (side > best) {
            best = side;
            count = 1;
        } else if (side == best) {
            count++;
        }
    }
    return count;
}
