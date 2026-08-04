// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int[] c = new int[2];
        for (int s : students) c[s]++;
        for (int i = 0; i < sandwiches.length; i++) {
            int x = sandwiches[i];
            if (c[x] == 0) return students.length - i;
            c[x]--;
        }
        return 0;
    }
}
