// LeetCode 1402: Reducing Dishes

var maxSatisfaction = function(satisfaction) {
    satisfaction.sort((a, b) => b - a);
    let prefix = 0, answer = 0;
    for (const value of satisfaction) { prefix += value; if (prefix <= 0) break; answer += prefix; }
    return answer;
};
