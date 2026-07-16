public class Solution
{
    public int TrailingZeroes(int n)
    {
        var count = 0;
        while (n > 0)
        {
            n /= 5;
            count += n;
        }
        return count;
    }
}
