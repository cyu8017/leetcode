// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        sort(meetings.begin(), meetings.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) {
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        };
        auto unite = [&](int a, int b) {
            a = find(a); b = find(b);
            if (a != b) parent[a] = b;
        };
        vector<char> know(n);
        know[0] = know[firstPerson] = 1;
        unite(0, firstPerson);
        for (int i = 0; i < (int)meetings.size(); ) {
            int j = i;
            while (j < (int)meetings.size() && meetings[j][2] == meetings[i][2]) j++;
            for (int k = i; k < j; k++) unite(meetings[k][0], meetings[k][1]);
            int root0 = find(0);
            vector<int> reset;
            for (int k = i; k < j; k++) {
                int a = meetings[k][0], b = meetings[k][1];
                if (find(a) != root0) { reset.push_back(a); reset.push_back(b); }
                else { know[a] = know[b] = 1; }
            }
            for (int x : reset) parent[x] = x;
            i = j;
        }
        vector<int> ans;
        for (int i = 0; i < n; i++) if (find(i) == find(0) || know[i]) ans.push_back(i);
        return ans;
    }
};
