// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

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

class SORTracker {
    struct Loc {
        string name;
        int score;
    };
    // min-heap: smaller score first; on tie, lexicographically larger name first
    struct MinCmp {
        bool operator()(const Loc& a, const Loc& b) const {
            if (a.score != b.score) return a.score > b.score;
            return a.name < b.name;
        }
    };
    // max-heap: larger score first; on tie, lexicographically smaller name first
    struct MaxCmp {
        bool operator()(const Loc& a, const Loc& b) const {
            if (a.score != b.score) return a.score < b.score;
            return a.name > b.name;
        }
    };
    priority_queue<Loc, vector<Loc>, MinCmp> best;
    priority_queue<Loc, vector<Loc>, MaxCmp> rest;
    int k = 0;
public:
    SORTracker() {}
    void add(string name, int score) {
        best.push({name, score});
        if ((int)best.size() > k) {
            rest.push(best.top());
            best.pop();
        }
    }
    string get() {
        k++;
        if (!rest.empty()) {
            best.push(rest.top());
            rest.pop();
        }
        return best.top().name;
    }
};
