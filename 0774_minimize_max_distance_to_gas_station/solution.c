// LeetCode 0774 - Minimize Max Distance to Gas Station
#include <math.h>

double minmaxGasDist(int* stations, int stationsSize, int k) {
    double lo = 0, hi = stations[stationsSize - 1] - stations[0];
    while (hi - lo > 1e-6) {
        double mid = (lo + hi) / 2;
        int need = 0;
        for (int i = 0; i < stationsSize - 1; i++) {
            need += (int)((stations[i + 1] - stations[i]) / mid);
        }
        if (need <= k) hi = mid; else lo = mid;
    }
    return hi;
}
