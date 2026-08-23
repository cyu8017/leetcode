// LeetCode 0362 - Design Hit Counter

// https://leetcode.com/problems/design-hit-counter/



public class HitCounter {

    private readonly LinkedList<int> hits = new();



    public HitCounter() {

    }



    public void Hit(int timestamp) {

        hits.AddLast(timestamp);

    }



    public int GetHits(int timestamp) {

        while (hits.Count > 0 && hits.First!.Value <= timestamp - 300) {

            hits.RemoveFirst();

        }

        return hits.Count;

    }

}
