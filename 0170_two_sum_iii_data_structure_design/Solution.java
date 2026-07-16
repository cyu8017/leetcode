import java.util.*;
class TwoSum {
    private final Map<Integer, Integer> counts = new HashMap<>();
    public void add(int number) { counts.put(number, counts.getOrDefault(number, 0) + 1); }
    public boolean find(int value) { for (Map.Entry<Integer, Integer> entry : counts.entrySet()) { int number = entry.getKey(), complement = value - number; if (complement == number ? entry.getValue() >= 2 : counts.containsKey(complement)) return true; } return false; }
}