class Solution {
    public int maxProduct(int[] nums) {
        int best = nums[0], max = nums[0], min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int value = nums[i], previousMax = max, previousMin = min;
            max = Math.max(value, Math.max(previousMax * value, previousMin * value));
            min = Math.min(value, Math.min(previousMax * value, previousMin * value));
            best = Math.max(best, max);
        }
        return best;
    }
}