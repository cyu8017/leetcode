// LeetCode 1431 - Kids With The Greatest Number Of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for (int c : candies) max = Math.max(max, c);
        List<Boolean> answer = new ArrayList<>();
        for (int c : candies) answer.add(c + extraCandies >= max);
        return answer;
    }
}
