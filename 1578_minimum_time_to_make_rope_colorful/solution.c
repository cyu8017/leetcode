// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

int minCost(char* colors, int* neededTime, int neededTimeSize) {
    int answer = 0, maximum = 0;
    for (int i = 0; i < neededTimeSize; i++) {
        if (i && colors[i] != colors[i - 1]) maximum = 0;
        int cost = neededTime[i];
        answer += maximum < cost ? maximum : cost;
        if (cost > maximum) maximum = cost;
    }
    return answer;
}
