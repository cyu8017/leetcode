public class Solution {
    public int Rob(int[] nums) {
        var previousTwo = 0;
        var previousOne = 0;
        foreach (var num in nums) {
            var current = System.Math.Max(previousOne, previousTwo + num);
            previousTwo = previousOne;
            previousOne = current;
        }
        return previousOne;
    }
}
