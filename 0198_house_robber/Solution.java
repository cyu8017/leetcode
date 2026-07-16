class Solution {
    public int rob(int[] nums) {
        int previousTwo = 0;
        int previousOne = 0;
        for (int num : nums) {
            int current = Math.max(previousOne, previousTwo + num);
            previousTwo = previousOne;
            previousOne = current;
        }
        return previousOne;
    }
}
