// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    int sortArray(vector<int>& nums, vector<int>& pre) {
        int n = nums.size();
        string start = key(nums);
        vector<int> targetArr(n);
        for (int i = 0; i < n; i++) targetArr[i] = i;
        string target = key(targetArr);
        if (start == target) return 0;

        vector<int> lengths;
        for (int i : pre) {
            if (i >= 2 && i <= n) lengths.push_back(i);
        }
        sort(lengths.begin(), lengths.end());
        lengths.erase(unique(lengths.begin(), lengths.end()), lengths.end());

        unordered_set<string> visited;
        visited.insert(start);
        queue<vector<int>> q;
        q.push(nums);
        int steps = 0;

        while (!q.empty()) {
            steps++;
            int size = q.size();
            for (int t = 0; t < size; t++) {
                vector<int> cur = q.front();
                q.pop();
                for (int i : lengths) {
                    vector<int> nxt = cur;
                    reverse(nxt.begin(), nxt.begin() + i);
                    string k = key(nxt);
                    if (k == target) return steps;
                    if (visited.insert(k).second) q.push(nxt);
                }
            }
        }
        return -1;
    }

private:
    string key(const vector<int>& arr) {
        string s;
        for (int i = 0; i < (int)arr.size(); i++) {
            if (i) s.push_back(',');
            s += to_string(arr[i]);
        }
        return s;
    }
};
