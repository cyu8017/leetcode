// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

int minCostToMoveChips(int* position, int positionSize) {
    int odd = 0;
    for (int i = 0; i < positionSize; i++) odd += position[i] & 1;
    int even = positionSize - odd;
    return odd < even ? odd : even;
}
