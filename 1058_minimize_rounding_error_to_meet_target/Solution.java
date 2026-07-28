// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public String minimizeError(String[] prices, int target) {
        int floors = 0;
        List<Double> fracs = new ArrayList<>();
        for (String p : prices) {
            double value = Double.parseDouble(p);
            int floor = (int) value;
            floors += floor;
            double frac = value - floor;
            if (frac > 1e-9) {
                fracs.add(frac);
            }
        }
        int ceilCount = target - floors;
        if (ceilCount < 0 || ceilCount > fracs.size()) {
            return "-1";
        }
        fracs.sort(Collections.reverseOrder());
        double error = 0.0;
        for (int i = 0; i < fracs.size(); i++) {
            double f = fracs.get(i);
            if (i < ceilCount) {
                error += 1 - f;
            } else {
                error += f;
            }
        }
        return String.format("%.3f", error);
    }
}
