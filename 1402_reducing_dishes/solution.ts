// LeetCode 1402: Reducing Dishes

function maxSatisfaction(satisfaction: any): any {
    satisfaction.sort((a, b: any): any => b - a);
    let prefix = 0, answer = 0;
    for (const value of satisfaction) { prefix += value; if (prefix <= 0) break; answer += prefix; }
    return answer;
}
