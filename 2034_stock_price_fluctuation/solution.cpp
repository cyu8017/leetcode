// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

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

class StockPrice {
    int latestTs = 0;
    unordered_map<int, int> priceAt;
    priority_queue<pair<int,int>> maxHeap;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap;
public:
    StockPrice() {}
    void update(int timestamp, int price) {
        priceAt[timestamp] = price;
        if (timestamp >= latestTs) latestTs = timestamp;
        maxHeap.push({price, timestamp});
        minHeap.push({price, timestamp});
    }
    int current() { return priceAt[latestTs]; }
    int maximum() {
        while (true) {
            auto [price, ts] = maxHeap.top();
            if (priceAt[ts] == price) return price;
            maxHeap.pop();
        }
    }
    int minimum() {
        while (true) {
            auto [price, ts] = minHeap.top();
            if (priceAt[ts] == price) return price;
            minHeap.pop();
        }
    }
};
