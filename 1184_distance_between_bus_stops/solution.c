// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

int distanceBetweenBusStops(int* distance, int distanceSize, int start, int destination) {
    if (start > destination) {
        int tmp = start;
        start = destination;
        destination = tmp;
    }
    int clockwise = 0;
    for (int i = start; i < destination; i++) clockwise += distance[i];
    int total = 0;
    for (int i = 0; i < distanceSize; i++) total += distance[i];
    return clockwise < total - clockwise ? clockwise : total - clockwise;
}
